"""Clean, transform, and merge raw datasets into analysis-ready data.

Intended pipeline role:
1. Load files from `data/raw/`.
2. Apply cleaning and harmonization rules.
3. Merge sources and write outputs to `data/processed/`.
"""

from pathlib import Path


def main() -> None:
    """Entry point for dataset construction."""
    processed_dir = Path(__file__).resolve().parents[1] / "data" / "processed"
    processed_dir.mkdir(parents=True, exist_ok=True)
    print(f"Processed data directory ready: {processed_dir}")
    print("TODO: Implement cleaning and merge pipeline.")


if __name__ == "__main__":
    main()
