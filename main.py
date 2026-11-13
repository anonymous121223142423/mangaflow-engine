import argparse
import json
import os
import zipfile
from pathlib import Path
from typing import Dict, List


class MangaLibraryManager:
    """Core engine for scanning, validating, and indexing digital manga archives."""

    SUPPORTED_EXTENSIONS = {".cbz", ".zip"}

    def __init__(self, library_path: str):
        self.library_path = Path(library_path)
        self.catalog: List[Dict] = []

    def scan_directory(self) -> List[Dict]:
        """Scans the target directory for valid comic archives."""
        if not self.library_path.exists():
            raise FileNotFoundError(f"Directory not found: {self.library_path}")

        for root, _, files in os.walk(self.library_path):
            for file in sorted(files):
                file_path = Path(root) / file
                if file_path.suffix.lower() in self.SUPPORTED_EXTENSIONS:
                    metadata = self._extract_archive_info(file_path)
                    if metadata:
                        self.catalog.append(metadata)

        return self.catalog

    def _extract_archive_info(self, archive_path: Path) -> Dict:
        """Validates archive integrity and counts readable image pages."""
        image_extensions = {".jpg", ".jpeg", ".png", ".webp"}
        try:
            with zipfile.ZipFile(archive_path, "r") as zf:
                pages = [
                    name
                    for name in zf.namelist()
                    if Path(name).suffix.lower() in image_extensions
                    and not name.startswith("__MACOSX")
                ]
                return {
                    "series": archive_path.parent.name,
                    "chapter_file": archive_path.name,
                    "page_count": len(pages),
                    "size_mb": round(archive_path.stat().st_size / (1024 * 1024), 2),
                    "status": "valid" if pages else "empty",
                }
        except zipfile.BadZipFile:
            return {
                "series": archive_path.parent.name,
                "chapter_file": archive_path.name,
                "page_count": 0,
                "size_mb": 0,
                "status": "corrupted",
            }

    def export_index(self, output_file: str = "library_index.json") -> None:
        """Exports the scanned library metadata to a clean JSON index."""
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(self.catalog, f, indent=4, ensure_ascii=False)
        print(f"Successfully indexed {len(self.catalog)} archives into {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description="MangaFlow Engine - Digital Manga Library Organizer"
    )
    parser.add_argument(
        "--scan",
        type=str,
        default="./library",
        help="Path to the manga library folder",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="library_index.json",
        help="Output JSON metadata filename",
    )
    args = parser.parse_args()

    manager = MangaLibraryManager(args.scan)
    print(f"Scanning directory: {args.scan}...")
    try:
        manager.scan_directory()
        manager.export_index(args.output)
    except FileNotFoundError as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()
