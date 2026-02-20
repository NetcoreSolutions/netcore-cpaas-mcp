"""WhatsApp Miscellaneous APIs — settings, stats, messages, API status."""

from netcore_whatsapp import MISC_BASE_URL, api_get


# ---------------------------------------------------------------------------
# Get Settings
# ---------------------------------------------------------------------------
def fetch_whatsapp_settings() -> dict:
    """Retrieve the current settings for the WhatsApp Business Account."""
    url = f"{MISC_BASE_URL}/settings"
    return api_get(url)


# ---------------------------------------------------------------------------
# Get Statistics
# ---------------------------------------------------------------------------
def fetch_whatsapp_stats(
    start_date: str, end_date: str, granularity: str = None
) -> dict:
    """Retrieve statistics data for WhatsApp messages within a date range.

    Args:
        start_date: Start date (YYYY-MM-DD format).
        end_date: End date (YYYY-MM-DD format).
        granularity: Granularity of data — "day", "week", or "month".
    """
    url = f"{MISC_BASE_URL}/stats"
    params = {"start_date": start_date, "end_date": end_date}
    if granularity:
        params["granularity"] = granularity
    return api_get(url, params=params)


# ---------------------------------------------------------------------------
# Get Messages
# ---------------------------------------------------------------------------
def fetch_whatsapp_messages(start_date: str, end_date: str) -> dict:
    """Retrieve message details for WhatsApp messages within a date range.

    Args:
        start_date: Start date (YYYY-MM-DD format).
        end_date: End date (YYYY-MM-DD format).
    """
    url = f"{MISC_BASE_URL}/messages"
    params = {"start_date": start_date, "end_date": end_date}
    return api_get(url, params=params)


# ---------------------------------------------------------------------------
# Get Summary Statistics
# ---------------------------------------------------------------------------
def fetch_summary_stats(tags: list = None) -> dict:
    """Retrieve summary statistics data filtered by tags.

    Args:
        tags: Optional list of tags to filter statistics.
    """
    url = f"{MISC_BASE_URL}/summary_stats"
    params = {}
    if tags:
        params["tags"] = tags
    return api_get(url, params=params)
    