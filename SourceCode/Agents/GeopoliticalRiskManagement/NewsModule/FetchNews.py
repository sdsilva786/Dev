import os
from SourceCode.Utilities.ConfigHelper import ReadAppConfigHelper as CH
import feedparser


def FetchNews():
    relative_path = CH.get_config("news_data")
    file_path = os.path.abspath(relative_path)
    feed = feedparser.parse(file_path)

    # Extract titles and summaries of top 5 entries
    entries = feed.entries[:5]
    news_data = "\n\n".join(
        f"Title: {entry.title}\nSummary: {entry.summary}" for entry in entries
    )

    return news_data
