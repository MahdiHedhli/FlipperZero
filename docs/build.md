# Build from the selected source

`firmware.lock.json` identifies the exact upstream revision. Keep upstream source under ignored `upstream/`, and keep our patches, application code and notes in this repository.

```sh
git clone --filter=blob:none --no-checkout https://github.com/DarkFlippers/unleashed-firmware.git upstream/unleashed
git -C upstream/unleashed checkout --detach 2f62b3ab5d767c41e09ab17c6b5fbd175c8c4c85
git -C upstream/unleashed submodule update --init --recursive
cd upstream/unleashed
./fbt
```

Review upstream build scripts and submodule origins before running a fresh checkout. FBT can download its toolchain. Follow the [pinned upstream documentation](https://github.com/DarkFlippers/unleashed-firmware/tree/unlshd-094/documentation) for platform-specific setup and distribution targets.

These commands describe the source-build path; initial device setup uses the verified upstream release image. A local source build is not yet validated by this project, and byte-for-byte reproducibility has not been established.

For future changes, retain the exact base commit, record the patch, build with matching resources, test on owned lab fixtures, and preserve the official recovery path. Do not replace pinned releases with a moving development branch without a new review.
