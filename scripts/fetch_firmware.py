#!/usr/bin/env python3
"""Download and verify a pinned firmware image; never connect to or flash a device."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile
from urllib.parse import urlparse
from urllib.request import urlopen


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--official", action="store_true", help="Fetch the official recovery image")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    lock = json.loads((root / "firmware.lock.json").read_text())
    entry = lock["official_prerequisite_and_recovery"] if args.official else lock["asset"]
    url = entry["url"]
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.hostname not in {"github.com", "update.flipperzero.one"}:
        raise SystemExit("Unexpected download origin; review the lock file.")
    digest = entry["sha256"]
    if not re.fullmatch(r"[0-9a-f]{64}", digest):
        raise SystemExit("Invalid pinned SHA-256.")
    name = parsed.path.rsplit("/", 1)[-1]
    if not re.fullmatch(r"flipper-z-f7-update-[A-Za-z0-9._-]+\.tgz", name):
        raise SystemExit("Unexpected image name or hardware target.")
    destination = root / "downloads" / name
    destination.parent.mkdir(exist_ok=True)
    if destination.exists():
        hasher = hashlib.sha256()
        with destination.open("rb") as existing:
            while chunk := existing.read(1024 * 1024):
                hasher.update(chunk)
        actual = hasher.hexdigest()
        if actual != digest:
            raise SystemExit("Existing image checksum mismatch; inspect it before replacing it.")
        print(f"Verified existing image: {destination.name}\nSHA-256: {digest}")
        return
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=destination.parent, delete=False) as target:
            temporary = Path(target.name)
            hasher = hashlib.sha256()
            received = 0
            with urlopen(url, timeout=60) as response:
                if urlparse(response.url).scheme != "https":
                    raise RuntimeError("Refusing a non-HTTPS redirect")
                while chunk := response.read(1024 * 1024):
                    received += len(chunk)
                    if received > 64 * 1024 * 1024:
                        raise RuntimeError("Image exceeds the expected size limit")
                    hasher.update(chunk)
                    target.write(chunk)
            if hasher.hexdigest() != digest:
                raise RuntimeError("SHA-256 mismatch; image will not be retained")
            if "bytes" in entry and received != entry["bytes"]:
                raise RuntimeError("Image size differs from the pinned release")
        os.replace(temporary, destination)
        print(f"Downloaded and verified: {destination.name}\nSHA-256: {digest}")
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
