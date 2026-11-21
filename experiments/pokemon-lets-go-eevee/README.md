# Pokémon: Let's Go, Eevee! — experimental scaffold

- Base title ID: `0100187003A36000`
- Target update: `v1.0.2`
- Status: metadata-only scaffold; **not a runnable game profile**
- Private inputs: none. No NSP, prod.keys, firmware, extracted game files, build IDs, or shader data are stored here.

## Why this is outside dm/games

The Peanuts Native profile loader discovers profiles only under `dm/games/<16-hex-title-id>/game.tsv`. A guessed profile placed there could be mistaken for a real supported profile and could fail at runtime. This scaffold is deliberately kept under `experiments/` so it cannot be selected by the app or included in a release.

## Known unknowns

The following must come from a real survey of the user's own base game + update v1.0.2 and cannot safely be inferred from another Pokémon title:

- NSO build IDs for `main` and `sdk` (and any imported modules)
- SDK / engine identification and exact module list
- RomFS marker and shader container layout
- memory reservation / alias / app-pool measurements
- shader tables and pipeline prewarm data
- any build-specific rewrite patches

Pokémon Legends: Arceus and Pokémon Legends: Z-A are useful architectural references, but their build IDs, memory settings, shader tables, and patches must **not** be copied into this game's profile.

## What the workflow does

The workflow validates this metadata-only scaffold and runs the repository's existing profile/runtime checks. It does not process game files and does not build a playable Let's Go APK. An APK built without a valid profile and shader package would not demonstrate game compatibility.

## Next safe step

Run a local survey against the user's own encrypted NSPs using their own keys, keeping all game data on their device. Only non-secret survey facts (module/build IDs and SDK/engine summary) need to be shared if the user chooses to continue. Never upload the NSP, prod.keys, or firmware to this repository or a public Actions artifact.
