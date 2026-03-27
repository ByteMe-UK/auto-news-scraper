"""
Fetches top stories from the HackerNews Algolia Search API.

Algolia HN API (public, no auth, single request returns full story details):
  https://hn.algolia.com/api/v1/search?tags=front_page&hitsPerPage=N
"""

import logging

import requests

logger = logging.getLogger(__name__)

ALGOLIA_URL = "https://hn.algolia.com/api/v1/search"
TIMEOUT = 15


def fetch_top_stories(limit: int = 30) -> list[dict]:
    """
    Fetch the top N HackerNews front page stories via Algolia API.

    Returns a list of story dicts with keys:
      id, title, url, score, by, descendants
    """
    params = {
        "tags": "front_page",
        "hitsPerPage": limit,
    }
    resp = requests.get(ALGOLIA_URL, params=params, timeout=TIMEOUT)
    resp.raise_for_status()

    hits = resp.json().get("hits", [])

    stories = []
    for hit in hits:
        stories.append({
            "id":          hit.get("objectID", ""),
            "title":       hit.get("title", "No title"),
            "url":         hit.get("url", ""),
            "score":       hit.get("points", 0),
            "by":          hit.get("author", "unknown"),
            "descendants": hit.get("num_comments", 0),
        })

    return stories
