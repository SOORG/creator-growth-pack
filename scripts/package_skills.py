#!/usr/bin/env python3
"""Build deterministic, one-skill-per-ZIP archives using only the stdlib."""
from __future__ import annotations

import argparse
import tempfile
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
EXPECTED = (
    "creator-outreach",
    "creator-profile-setup",
    "product-listing-copy",
    "social-content-engine",
)


def build(output: Path) -> list[Path]:
    output.mkdir(parents=True, exist_ok=True)
    outputs: list[Path] = []
    for name in EXPECTED:
        skill = SKILLS / name
        if not (skill / "SKILL.md").is_file():
            raise ValueError(f"Missing entrypoint for {name}")
        target = output / f"{name}.zip"
        with ZipFile(target, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
            for file in sorted(skill.rglob("*")):
                if not file.is_file():
                    continue
                if file.is_symlink() or "__pycache__" in file.parts:
                    raise ValueError(f"Unsafe package member: {file}")
                relative = file.relative_to(skill).as_posix()
                info = ZipInfo(relative, date_time=(2020, 1, 1, 0, 0, 0))
                info.compress_type = ZIP_DEFLATED
                info.external_attr = 0o644 << 16
                archive.writestr(info, file.read_bytes(), compress_type=ZIP_DEFLATED, compresslevel=9)
        with ZipFile(target) as archive:
            names = archive.namelist()
            if "SKILL.md" not in names or archive.testzip() is not None:
                raise ValueError(f"Bad generated ZIP: {target}")
        outputs.append(target)
    return outputs


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "dist")
    parser.add_argument("--check", action="store_true", help="test without leaving output archives")
    args = parser.parse_args()
    if args.check:
        with tempfile.TemporaryDirectory(prefix="cgp-package-") as temp:
            packages = build(Path(temp))
            print(f"PASS: {len(packages)} valid, standalone skill ZIP archives")
    else:
        packages = build(args.output)
        for package in packages:
            print(package)


if __name__ == "__main__":
    main()
