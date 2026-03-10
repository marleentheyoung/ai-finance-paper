"""Download or import raw financial datasets.

Intended pipeline role:
1. Define source endpoints, file paths, and credentials if needed.
2. Pull raw files into `data/raw/`.
3. Log metadata (download date, source URL, version).
"""

from pathlib import Path


def main() -> None:
    """Entry point for raw data acquisition."""
    raw_dir = Path(__file__).resolve().parents[1] / "data" / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    print(f"Raw data directory ready: {raw_dir}")
    print("TODO: Implement data download/import logic.")


if __name__ == "__main__":
    main()
