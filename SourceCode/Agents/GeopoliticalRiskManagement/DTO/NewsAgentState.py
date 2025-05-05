from typing import Optional, TypedDict


class NewsAgentState(TypedDict):
    news_text: Optional[str]
    summary: Optional[str]
