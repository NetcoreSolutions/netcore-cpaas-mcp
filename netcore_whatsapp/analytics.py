"""WhatsApp Analytics APIs — fetch template performance metrics."""

from netcore_whatsapp import BASE_URL, api_get


# ---------------------------------------------------------------------------
# Fetch Template Analytics (v3)
# ---------------------------------------------------------------------------
def fetch_template_analytics(
    template_id: str,
    date_start: str,
    date_end: str,
    nc_template_id: str = None,
    granularity: str = None,
    limit: int = None,
    use_waba_timezone: bool = None,
    product_type: str = None,
    after: str = None,
    before: str = None,
    metric_types: str = None,
) -> dict:
    """Fetch analytics metrics for one or more WhatsApp templates.

    Args:
        template_id: Comma-separated Meta template IDs (up to 10).
        date_start: Start date in YYYY-MM-DD format.
        date_end: End date in YYYY-MM-DD format.
        nc_template_id: Netcore template ID (single value).
        granularity: Time grouping (e.g. "DAILY").
        limit: Max records per page.
        use_waba_timezone: Use WABA timezone for metrics.
        product_type: Filter by product type (CLOUD_API or MARKETING_MESSAGES_LITE_API).
        after: Cursor for next page.
        before: Cursor for previous page.
        metric_types: Comma-separated metric names to return.
    """
    url = f"{BASE_URL}/v3/metainfo/template/analytics"
    params = {
        "template_id": template_id,
        "date_start": date_start,
        "date_end": date_end,
    }
    if nc_template_id:
        params["nc_template_id"] = nc_template_id
    if granularity:
        params["granularity"] = granularity
    if limit is not None:
        params["limit"] = limit
    if use_waba_timezone is not None:
        params["use_waba_timezone"] = use_waba_timezone
    if product_type:
        params["product_type"] = product_type
    if after:
        params["after"] = after
    if before:
        params["before"] = before
    if metric_types:
        params["metric_types"] = metric_types
    return api_get(url, params=params)
