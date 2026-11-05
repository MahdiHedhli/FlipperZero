# Firmware selection review

Reviewed November 5, 2026. Unleashed `unlshd-094` is selected for this lab's broader testing features and recent stable maintenance. Official 1.5.1 remains the vendor-supported alternative. This decision is a practical fit assessment, not an assertion that any community firmware is universally the most secure.

## Provenance

- Release package downloaded from `DarkFlippers/unleashed-firmware` on GitHub.
- Package SHA-256 matched the GitHub release asset digest recorded in `firmware.lock.json`.
- The release resolves to commit `2f62b3ab5d767c41e09ab17c6b5fbd175c8c4c85`; GitHub's API reports its commit signature as verified.
- The official prerequisite/recovery image matched the vendor update directory's SHA-256.

These are upstream provenance and integrity checks, not an independent binary audit or a locally verified maintainer signing-key chain.

## Targeted source check

The selected Unleashed revision contains both bounds checks from [official firmware PR 4369](https://github.com/flipperdevices/flipperzero-firmware/pull/4369): the DESFire access-rights count limit and the Ultralight FAST_READ page-buffer limit. Checked in the pinned versions of `lib/nfc/protocols/mf_desfire/mf_desfire_i.c` and `lib/nfc/protocols/mf_ultralight/mf_ultralight_listener.c`.

This spot check does not establish complete patch parity, runtime exploit resistance or absence of other vulnerabilities. External boards and inherited third-party applications require separate assessment.
