"""WhatsApp Conversion Tracking APIs — CAPI events for Meta ad attribution."""

from netcore_whatsapp import BASE_URL, api_post


# ---------------------------------------------------------------------------
# Track Customer Conversions (CAPI) (v3)
# ---------------------------------------------------------------------------
def track_conversions(conversion_data: dict) -> dict:
    """Send conversion events to Meta for ad targeting and performance measurement.

    Supported events: Purchase, Lead, CompleteRegistration, Subscribe,
    StartTrial, AddToCart, InitiateCheckout, AddPaymentInfo, ViewContent, etc.

    Args:
        conversion_data: Dict with 'data' array of conversion event objects.
            Each event has: event_name, event_time, action_source,
            messaging_channel, user_data, and optional custom_data.
    """
    url = f"{BASE_URL}/v3/metainfo/dispatch_capi_event"
    return api_post(url, json_data=conversion_data)
