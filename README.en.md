# paper-harness-undergraduate

**Languages:** [简体中文](README.md) · [English](README.en.md) · [日本語](README.ja.md)

> A survey-first, auditable thesis workbench for undergraduate students and research beginners.

Start with a teacher-provided topic, turn local sources into traceable artifacts, design one bounded experiment, and write only claims that can be reviewed by a student and supervisor.

```bash
python -m paper_harness.cli init examples/stem_project/project.json --output ./runs/my-thesis
python -m paper_harness.cli run ./runs/my-thesis/project.json
```

The workflow pauses for approval before high-risk stages. It includes a local knowledge base, literature matrix, beginner experiment plan, claim audit, similarity screening and AI-use disclosure guidance. It does not bypass AI detection, fabricate citations, or replace formal plagiarism review.

See the [Chinese beginner guide](docs/getting-started-zh.md) and [undergraduate workflow notes](docs/undergraduate-edition-zh.md).
