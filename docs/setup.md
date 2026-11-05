# Installation and recovery

Use the official [Unleashed installation guide at the pinned tag](https://github.com/DarkFlippers/unleashed-firmware/blob/unlshd-094/documentation/HowToInstall.md).

1. Connect a charged Flipper Zero over a reliable USB cable with its microSD card installed. Close other applications using its USB connection.
2. Save an internal-storage backup with qFlipper. Back up personal SD data separately: qFlipper's internal backup is not a full SD-card backup. Store both privately, outside this repository.
3. Verify the firmware images using `scripts/fetch_firmware.py`. Select the F7 image; do not substitute an image for other hardware.
4. For a first Unleashed installation, update to official stable **1.5.1** first. Let it complete the radio, firmware and resource stages and reconnect.
5. In qFlipper, use **Install from file** with `flipper-z-f7-update-unlshd-094.tgz`. Alternatively, copy the complete extracted update directory to the SD card and launch its `update.fuf` as described upstream. Do not flash only the application image and omit its matching resources.
6. Wait for completion. Confirm the firmware reports `unlshd-094`, the SD card mounts, and matching applications are present. Inspect preserved user data without executing old scripts or payloads.

## Recovery

Keep the verified official image and private backup available. To return to official firmware, install the official F7 update package with qFlipper. If the application cannot boot, use qFlipper's documented firmware repair procedure. Do not erase internal storage or replace the firmware update service as a routine troubleshooting step.

Restore backups deliberately: old configuration formats can differ from current ones. The original SD-card contents are not fully covered by an internal backup. A firmware update is not a substitute for reviewing old third-party apps and payload collections.

## Validation limits

Successful flashing and boot checks establish that the package installs and starts. Protocol behavior, external boards and RF compliance need their own scoped lab tests. No nearby systems are tested during setup.
