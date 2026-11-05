# Security

This repository is public. Keep real device backups, NFC/RFID credentials, radio captures, authentication material, private identifiers and customer evidence outside the checkout. Publish only synthetic fixtures and deliberately redacted results.

Before pushing, inspect `git diff --cached` and `git diff --cached --name-only`. Ignored files can still be force-added; `.gitignore` does not inspect file contents. Never run unknown BadUSB/BadKB scripts or inherited third-party applications merely to check that they work.

Firmware images are obtained from their upstream projects and pinned by SHA-256. GitHub's verification of the source commit and the image's published checksum are distinct checks; neither establishes an independent security audit of the compiled image.

Use GitHub private vulnerability reporting if it is enabled. Do not include secrets or private captures in public issues. Upstream firmware vulnerabilities should also be reported through the affected upstream project's security process.

Keep a private issue register for unresolved findings that could expose sensitive information. Public issues should contain only sanitized descriptions. Record resolution evidence before closing a finding.
