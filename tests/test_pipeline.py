"""Smoke tests for the research pipeline template."""

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


def test_research_context_template_exists():
    root = Path(__file__).resolve().parents[1]
    assert (root / "context" / "research_context.md").exists()


def test_pipeline_map_exists():
    root = Path(__file__).resolve().parents[1]
    assert (root / "PIPELINE_MAP.md").exists()


def test_agent_definitions_exist():
    root = Path(__file__).resolve().parents[1]
    agents_dir = root / ".claude" / "agents"
    expected_agents = [
        "research-director.md",
        "literature-guardian.md",
        "research-evaluator.md",
        "theory-builder.md",
        "model-verifier.md",
        "paper-writer.md",
    ]
    for agent in expected_agents:
        assert (agents_dir / agent).exists(), f"Missing agent: .claude/agents/{agent}"


def test_no_generated_content_outside_archive():
    """Verify that project-specific generated content is not in the working directories."""
    root = Path(__file__).resolve().parents[1]
    # These files should only exist in archive/, not in context/
    generated_files = [
        "context/planning/research_plan.md",
        "context/literature/threat_map.md",
        "context/model_equations.md",
        "context/literature/review.md",
    ]
    for f in generated_files:
        assert not (root / f).exists(), f"Generated file should be archived: {f}"
