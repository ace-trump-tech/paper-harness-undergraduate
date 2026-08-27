from __future__ import annotations

from pathlib import Path

from .base import Agent, AgentContext, artifact
from ..knowledge import LocalKnowledgeBase
from ..models import AgentResult


class KnowledgeBaseAgent(Agent):
    name = "knowledge-base"

    def run(self, context: AgentContext) -> AgentResult:
        root = Path(context.project.root) / "knowledge" if context.project.root else None
        entries = []
        if root:
            entries = LocalKnowledgeBase(root).ingest_files(
                context.project.settings.get("knowledge_files", []),
                max_chars=int(context.project.settings.get("knowledge_chunk_chars", 6000)),
                overlap=int(context.project.settings.get("knowledge_chunk_overlap", 400)),
            )
        payload = {"root": str(root) if root else "memory://knowledge", "documents": entries, "document_count": len(entries), "chunking": {"max_chars": int(context.project.settings.get("knowledge_chunk_chars", 6000)), "overlap": int(context.project.settings.get("knowledge_chunk_overlap", 400))}, "long_text_policy": "store_chunks_on_disk; pass metadata to agents"}
        return AgentResult(self.name, "completed", [artifact("knowledge_index", context.project, self.name, payload, 0.7)], "Indexed local documents into bounded, persistent chunks.")


class UndergraduateGuideAgent(Agent):
    name = "undergraduate-guide"

    def run(self, context: AgentContext) -> AgentResult:
        payload = {"mode": "survey-first", "audience": "undergraduate thesis beginner", "workflow": ["define teacher-provided question", "build a structured review", "choose a feasible baseline", "run a bounded experiment", "check similarity and AI-use disclosure", "write and ask supervisor for confirmation"], "experiment_template": {"baseline": "teacher-approved baseline", "variables": ["one independent variable", "one evaluation metric", "one reproducible configuration"], "stop_rule": "stop when the planned comparison is complete"}, "human_checkpoints": ["scope approval", "source verification", "experiment design approval", "final academic integrity review"]}
        return AgentResult(self.name, "completed", [artifact("undergraduate_plan", context.project, self.name, payload, 0.8)], "Created a survey-first thesis plan with beginner checkpoints.")
