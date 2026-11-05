# Setup validation — November 5, 2026

## Installed baseline

| Check | Observed result |
| --- | --- |
| Initial official upgrade | qFlipper completed a full update to official 1.5.1; version confirmed after reconnect |
| Selected community release | Unleashed `unlshd-094` |
| Device-reported commit | `2f62b3ab`, matching the pinned upstream revision |
| Working tree marker | Firmware reports no dirty source tree |
| Hardware target | F7 / target 7 |
| Application API | 88.19 |
| Radio stack | 1.20.0, reports alive |
| microSD | Mounted and readable |
| Installed app resources | All 103 bundled FAPs matched the sizes and checksums in the installed resource manifest |
| Preserved user data | 32 selected top-level user files matched their pre-update backup checksums |

The community package's SHA-256 was verified before extraction. Every extracted update payload was compared with the verified archive, then checked for size and transfer integrity on the device before installation.

Internal settings and a targeted set of user data were backed up privately. This was not a full SD image; detailed scope and exceptions remain in the private backup report, outside this public repository.

## Repository checks

- Firmware downloader validated both pinned images.
- A clean download succeeded and matched the pinned digest.
- A deliberately corrupted local image was rejected.
- An insecure/unapproved download origin was rejected before download.
- Published files were reviewed; backups, captures, device identifiers and firmware binaries were excluded.
- GitHub reports the repository as public, with secret scanning, push protection and private vulnerability reporting enabled.

## Limits

Resource checks establish file integrity, not runtime behavior or a security audit of each app. No HID payload, RF transmission, credential emulation or external-board test was performed. Inherited SD content was not approved, audited or executed. A local firmware source build remains future work.
