# Android device-test APK

This workflow builds an installable, debug-signed **launcher/Vulkan test APK** for checking the Android app on a physical device.

It is deliberately isolated as package suffix `letsgo` so it installs beside other Banana Native / Peanuts Native builds rather than replacing them.

## Important limitation

This is **not a Pokémon: Let's Go, Eevee! game-support APK**. The repository does not yet have a surveyed or loadable profile for title ID `0100187003A36000`, and the game dump / keys are intentionally not uploaded to GitHub.

For a safe build-only test, the APK currently includes the repository's existing Ocarina of Time host profile (`0400486024DEC000`) and the fake on-device packer. It can be installed to inspect the launcher and run the graphics/Vulkan self-test, but it cannot prepare or launch Pokémon Let's Go, and its fake packer cannot create a playable game pack.

## Build and retrieve

1. Open the [device-test APK workflow](../../actions/workflows/letsgo-device-test-apk.yml).
2. Select **Run workflow** on branch `experiment/pokemon-lets-go-eevee-scaffold`, or wait for a push that changes Android source.
3. When the run succeeds, open its **Artifacts** section.
4. Download `peanuts-native-android-device-test` and extract `nxnative-android-letsgo.apk`.
5. Install it on the Poco F5. Its application ID is `dev.nxnative.android.letsgo`, so it should install separately from the normal test app.

The APK is debug-signed and intended only for local testing. Do not treat a successful APK build or Vulkan self-test as proof that Pokémon Let's Go is supported.

## Actual Pokémon Let's Go support still requires

A local survey of the user's own base NSP and update v1.0.2, using their own keys on their own device/computer. Only non-secret survey facts should be shared for profile development; never upload the NSP, keys, firmware, NUP, or extracted game files to this repository or workflow.
