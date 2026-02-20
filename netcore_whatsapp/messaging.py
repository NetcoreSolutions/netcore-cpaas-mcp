"""WhatsApp Message Sending APIs — template messages, priority messages, bulk upload."""

from netcore_whatsapp import BASE_URL, api_post, get_headers


# ---------------------------------------------------------------------------
# Send Template Message (v2)
# ---------------------------------------------------------------------------
def send_template_message(message_payload: dict) -> dict:
    """Send a WhatsApp template message (text, media, coupon, carousel, interactive, etc.).

    The payload structure determines the template type. Pass the full message
    payload as described in the API docs.

    Args:
        message_payload: Full request body dict. Must contain a 'message' array
            with recipient, message_type, type_template, etc.
    """
    url = f"{BASE_URL}/v2/message/nc"
    return api_post(url, json_data=message_payload)
