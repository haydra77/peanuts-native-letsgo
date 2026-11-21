#!/usr/bin/env python3
"""Validate the metadata-only Let's Go scaffold; this is not a game-profile validator."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "experiments/pokemon-lets-go-eevee"
manifest = BASE / "profile.template.tsv"
readme = BASE / "README.md"

rows = {}
for line in manifest.read_text(encoding="utf-8").splitlines():
    if not line or line.startswith("#"):
        continue
    key, value = line.split("\t", 1)
    rows.setdefault(key, []).append(value)

assert rows.get("title_id") == ["0100187003A36000"], rows.get("title_id")
assert rows.get("program_id") == ["0100187003A36000"], rows.get("program_id")
assert rows.get("target_update") == ["v1.0.2"], rows.get("target_update")
assert rows.get("status") == ["metadata_only_not_loadable"], rows.get("status")
assert not re.fullmatch(r"[0-9a-f]{32}", rows.get("fake_build_id", [""])[0]), "Do not add fabricated build IDs"

# The scaffold must stay outside dm/games, and no game dumps/keys are expected in the checkout.
assert not (ROOT / "dm/games/0100187003A36000").exists(), "Do not register an unverified profile"
for pattern in ("*.nsp", "*.nsz", "*.xci", "*.xcz", "prod.keys", "*.nup"):
    found = list(ROOT.rglob(pattern))
    assert not found, f"Unexpected private game input in repository checkout: {pattern}: {found[:3]}"

text = readme.read_text(encoding="utf-8")
assert "not a runnable game profile" in text
assert "No NSP, prod.keys" in text
print("OK: Let's Go metadata scaffold is valid and contains no game dump or keys.")
