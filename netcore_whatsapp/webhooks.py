"""WhatsApp Webhook Management APIs — list, update, manage status."""

from netcore_whatsapp import BASE_URL, api_get, api_post


# ---------------------------------------------------------------------------
# List Webhooks (v3)
# ---------------------------------------------------------------------------
def fetch_webhook_list(webhook_type: str) -> dict:
    """Retrieve all configured webhooks of a given type.

    Args:
        webhook_type: Webhook type — "incoming" or "event".
    """
    url = f"{BASE_URL}/v3/metainfo/webhook/list_webhook"
    return api_get(url, params={"type": webhook_type})


# ---------------------------------------------------------------------------
# Update Webhook Configuration (v3)
# ---------------------------------------------------------------------------
def update_webhook(webhook_data: dict) -> dict:
    """Create or update a webhook configuration.

    Args:
        webhook_data: Dict with 'type' ("incoming"/"event"), 'name', 'url',
            optional 'source', and 'headers' (JSON string).
    """
    url = f"{BASE_URL}/v3/metainfo/webhook/update_webhook"
    return api_post(url, json_data=webhook_data)


# ---------------------------------------------------------------------------
# Manage Webhook Status (v2)
# ---------------------------------------------------------------------------
def manage_webhook_status(manage_data: dict) -> dict:
    """Enable or disable a webhook without changing its configuration.

    Args:
        manage_data: Dict with 'type' ("incoming"/"event"),
            'webhook_name', and 'status' ("enable"/"disable").
    """
    url = f"{BASE_URL}/v2/metainfo/webhook/manage_webhook"
    return api_post(url, json_data=manage_data)
