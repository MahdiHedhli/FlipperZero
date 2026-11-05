# FlipperZero

A reproducible starting point for Flipper Zero development and authorized security testing.

## Firmware baseline

**Unleashed `unlshd-094`, standard F7 package**, reviewed on November 5, 2026. This is a practical choice for broad NFC, RFID, infrared, GPIO and Sub-GHz lab work. It is community firmware, not a claim of independent security certification.

The [firmware lock](firmware.lock.json) pins the source commit, release image and SHA-256 digest. Official **1.5.1** is the first-install prerequisite and recovery baseline. The setup does not require the optional extra-app bundle.

Installation on F7 hardware completed successfully; see the [validation record](docs/validation.md).

| Option | Stable release checked | Role in this project |
| --- | --- | --- |
| [Unleashed](https://github.com/DarkFlippers/unleashed-firmware/releases/tag/unlshd-094) | `unlshd-094`, October 14, 2026 | Selected for expanded testing capabilities and recent maintenance |
| [Official firmware](https://github.com/flipperdevices/flipperzero-firmware/releases/tag/1.5.1) | `1.5.1`, October 15, 2026 | Vendor-supported baseline and recovery route |
| [Momentum](https://github.com/Next-Flip/Momentum-Firmware/releases/tag/mntm-012) | `mntm-012`, December 31, 2025 | Useful customization; its latest stable release is older |

Unleashed removes regional transmission restrictions. Configure every RF experiment for the permitted band, power and equipment; firmware capability is not permission to transmit. No transmit test is part of initial installation.

## Get the pinned images

Requires Python 3; no third-party Python packages:

```sh
python3 scripts/fetch_firmware.py
python3 scripts/fetch_firmware.py --official
```

Downloads remain in ignored `downloads/`. The script checks the pinned SHA-256 and never flashes a device. A matching digest establishes consistency with the release metadata, not independent proof that firmware is vulnerability-free.

## Work here

- [Installation and recovery](docs/setup.md)
- [Firmware selection and security checks](docs/firmware-review.md)
- [Building from the pinned source](docs/build.md)
- [Lab scope template](examples/lab-scope.md)
- [Security and private-data handling](SECURITY.md)

Keep backups, captures, pairing material and device identifiers outside this public repository. `.gitignore` is a convenience, not a security boundary; review staged content before every push.

The Flipper itself has no Wi-Fi radio. Wi-Fi work requires a compatible external board and separately reviewed board firmware.

Original project files use GPL-3.0. Upstream firmware, applications and assets retain their respective licenses; firmware binaries are linked, not redistributed here.
