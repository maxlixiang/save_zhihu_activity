from __future__ import annotations

import argparse
from itertools import chain
from pathlib import Path


IMAGE_SUFFIX = "_图片"


def iter_rename_candidates(root: Path):
    for current_dir in chain([root], sorted(root.rglob("*"))):
        if not current_dir.is_dir():
            continue

        md_stems = {path.stem for path in current_dir.glob("*.md") if path.is_file()}
        if not md_stems:
            continue

        for child_dir in sorted(path for path in current_dir.iterdir() if path.is_dir()):
            if not child_dir.name.endswith(IMAGE_SUFFIX):
                continue

            target_name = child_dir.name[: -len(IMAGE_SUFFIX)]
            if target_name not in md_stems:
                yield child_dir, None, "no matching md file"
                continue

            yield child_dir, child_dir.with_name(target_name), None


def rename_folder(source: Path, destination: Path | None, reason: str | None, apply: bool) -> str:
    if destination is None:
        return f"SKIP {reason}: {source}"

    if destination.exists():
        return f"SKIP target exists: {source} -> {destination}"

    if not apply:
        return f"DRY  rename: {source} -> {destination}"

    source.rename(destination)
    return f"DONE rename: {source} -> {destination}"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Rename *_图片 folders to match sibling Markdown file names."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent,
        help="Archive repository root. Defaults to this script's directory.",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually rename folders. Without this flag the script only prints a dry run.",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    if not root.exists():
        raise SystemExit(f"Root path does not exist: {root}")
    if not root.is_dir():
        raise SystemExit(f"Root path is not a directory: {root}")

    renamed_or_planned = 0
    skipped = 0

    print(f"Archive root: {root}")
    print(f"Mode: {'APPLY' if args.apply else 'DRY RUN'}")
    print("")

    for source, destination, reason in iter_rename_candidates(root):
        result = rename_folder(source, destination, reason, apply=args.apply)
        print(result)
        if result.startswith(("DRY", "DONE")):
            renamed_or_planned += 1
        elif result.startswith("SKIP"):
            skipped += 1

    print("")
    print(f"Renamed/planned folders: {renamed_or_planned}")
    print(f"Skipped folders: {skipped}")

    if not args.apply:
        print("")
        print("Dry run only. Re-run with --apply to rename folders.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
