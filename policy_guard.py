from __future__ import annotations

import re
from typing import Any

# Deliberately conservative. False positives are acceptable because the purpose
# is to prevent autonomous political/electoral forecasting, not maximize volume.
_BLOCK_PATTERNS = [
    r"\belection(s| day)?\b",
    r"\belectoral\b",
    r"\bballot\b",
    r"\breferendum\b",
    r"\bcandidate(s)?\b",
    r"\bcampaign(s|ing)?\b",
    r"\bpresident(ial)?\b",
    r"\bprime minister\b",
    r"\bgovernor\b",
    r"\bmayor(al)?\b",
    r"\bsenator(s)?\b",
    r"\bcongress(man|woman|ional)?\b",
    r"\bparliament(ary)?\b",
    r"\bpolitical party\b",
    r"\bdemocrat(ic)?\b",
    r"\brepublican\b",
    r"\blabou?r party\b",
    r"\bconservative party\b",
    r"\bvote(r|rs|d|s|ing)?\b",
    r"\bnominee\b",
    r"\bwhite house\b",
]
_BLOCK_RE = re.compile("|".join(_BLOCK_PATTERNS), flags=re.IGNORECASE)


def is_blocked_forecast_topic(text: str) -> bool:
    return bool(_BLOCK_RE.search(text or ""))


def question_text_blob(question: Any) -> str:
    fields = (
        "question_text",
        "background_info",
        "resolution_criteria",
        "fine_print",
        "description",
    )
    return "\n".join(str(getattr(question, name, "") or "") for name in fields)


def should_block_question(question: Any) -> bool:
    return is_blocked_forecast_topic(question_text_blob(question))
