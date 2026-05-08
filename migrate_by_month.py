from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


DATE_PREFIX_RE = re.compile(r"^\[(?P<year>\d{4})-(?P<month>\d{2})-\d{2}_\d{2}-\d{2}\]")
YEAR_DIR_RE = re.compile(r"^\d{4}$")
MONTH_DIR_RE = re.compile(r"^\d{2}$")


def parse_target_month(path: Path) -> tuple[str, str] | None:
    match = DATE_PREFIX_RE.match(path.name)
    if not match:
        return None
    return match.group("year"), match.group("month")


def iter_archive_items(root: Path):
    for year_dir in sorted(root.iterdir()):
        if not year_dir.is_dir() or not YEAR_DIR_RE.match(year_dir.name):
            continue

        for item in sorted(year_dir.iterdir()):
            if item.is_dir() and MONTH_DIR_RE.match(item.name):
                continue

            parsed = parse_target_month(item)
            if parsed is None:
                yield item, None
                continue

            year, month = parsed
            if year != year_dir.name:
                yield item, None
                continue

            yield item, year_dir / month / item.name


def iter_import_items(source_dir: Path, archive_root: Path):
    for item in sorted(source_dir.iterdir()):
        parsed = parse_target_month(item)
        if parsed is None:
            yield item, None
            continue

        year, month = parsed
        yield item, archive_root / year / month / item.name


def move_item(source: Path, destination: Path, apply: bool) -> str:
    if destination.exists():
        return f"SKIP exists: {source} -> {destination}"

    if not apply:
        return f"DRY  move:   {source} -> {destination}"

    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(source), str(destination))
    return f"MOVE done:   {source} -> {destination}"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Move Zhihu archive files into YYYY/MM/ folders."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent,
        help="Archive repository root. Defaults to this script's directory.",
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=None,
        help=(
            "Import folder containing archive items to file into YYYY/MM/. "
            "Defaults to ROOT/test when that folder exists."
        ),
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually move files. Without this flag the script only prints a dry run.",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    if not root.exists():
        raise SystemExit(f"Root path does not exist: {root}")
    if not root.is_dir():
        raise SystemExit(f"Root path is not a directory: {root}")

    source = args.source
    if source is None:
        default_source = root / "test"
        source = default_source if default_source.exists() else None
    else:
        source = source.resolve()
        if not source.exists():
            raise SystemExit(f"Source path does not exist: {source}")
        if not source.is_dir():
            raise SystemExit(f"Source path is not a directory: {source}")

    moved_or_planned = 0
    skipped_unmatched = 0

    print(f"Archive root: {root}")
    print(f"Import source: {source if source is not None else '(none)'}")
    print(f"Mode: {'APPLY' if args.apply else 'DRY RUN'}")
    print("")

    for source_item, destination in iter_archive_items(root):
        if destination is None:
            skipped_unmatched += 1
            print(f"SKIP unmatched: {source_item}")
            continue

        result = move_item(source_item, destination, apply=args.apply)
        print(result)
        if result.startswith(("DRY", "MOVE")):
            moved_or_planned += 1

    if source is not None:
        for source_item, destination in iter_import_items(source, root):
            if destination is None:
                skipped_unmatched += 1
                print(f"SKIP unmatched: {source_item}")
                continue

            result = move_item(source_item, destination, apply=args.apply)
            print(result)
            if result.startswith(("DRY", "MOVE")):
                moved_or_planned += 1

    print("")
    print(f"Moved/planned items: {moved_or_planned}")
    print(f"Skipped unmatched items: {skipped_unmatched}")

    if not args.apply:
        print("")
        print("Dry run only. Re-run with --apply to move files.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
