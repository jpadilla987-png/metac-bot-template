from __future__ import annotations

import re
from typing import Any

# Deliberately conservative. False positives are acceptable because this bot must
# never autonomously generate or publish political/electoral forecasts.
_BLOCK_PATTERNS = [
    r"\belection(s| day)?\b",
    r"\belectoral\b",
    r"\bballot\b",
    r"\breferendum\b",
    r"\bcandidate(s)?\b",
    r"\bcampaign(s|ing)?\b",
    r"\bpresident(ial)?\b",
    r"\bprime minister\b",
    r"\bminister(s|ial)?\b",
    r"\bgovernor\b",
    r"\bmayor(al)?\b",
    r"\bsenator(s)?\b",
    r"\bcongress(man|woman|ional)?\b",
    r"\bparliament(ary)?\b",
    r"\bpolitic(s|al|ally)?\b",
    r"\bpolitical party\b",
    r"\bdemocrat(ic)?\b",
    r"\brepublican\b",
    r"\blabou?r party\b",
    r"\bconservative party\b",
    r"\bvote(r|rs|d|s|ing)?\b",
    r"\bnominee\b",
    r"\bwhite house\b",
    r"\bgovernment(s|al)?\b",
    r"\bcabinet\b",
    r"\blegislat(e|ion|ive|ure)\b",
    r"\blawmakers?\b",
    r"\bpublic policy\b",
    r"\bsupreme court\b",
    r"\bgeopolitic(s|al|ally)?\b",
    r"\bsanction(s|ed|ing)?\b",
    r"\btreat(y|ies)\b",
    r"\barticle\s*50\b",
    r"\b(leave|exit|withdraw from|join|rejoin)\s+(the\s+)?(eu|european union|nato|united nations)\b",
]
_BLOCK_RE = re.compile("|".join(_BLOCK_PATTERNS), flags=re.IGNORECASE)


def is_blocked_forecast_topic(text: str) -> bool:
    return bool(_BLOCK_RE.search(text or ""))


def question_text_blob(question: Any) -> str:
    # Include likely metadata fields as well as prose. If the SDK exposes a
    # Politics/Geopolitics tag/category, the guard should see it before a model call.
    fields = (
        "question_text",
        "title",
        "background_info",
        "resolution_criteria",
        "fine_print",
        "description",
        "category",
        "categories",
        "tags",
    )
    return "\n".join(str(getattr(question, name, "") or "") for name in fields)


def should_block_question(question: Any) -> bool:
    return is_blocked_forecast_topic(question_text_blob(question))
