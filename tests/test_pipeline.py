"""Smoke tests for the research pipeline scripts."""

from pathlib import Path


def test_project_root_exists():
    root = Path(__file__).resolve().parents[1]
    assert root.exists()


def test_code_scripts_exist():
    root = Path(__file__).resolve().parents[1]
    scripts = [
        "download_data.py",
        "build_dataset.py",
        "run_regressions.py",
        "generate_figures.py",
    ]
    for script in scripts:
        assert (root / "code" / script).exists(), f"Missing: code/{script}"


def test_paper_main_tex_exists():
    root = Path(__file__).resolve().parents[1]
    assert (root / "paper" / "main.tex").exists()
