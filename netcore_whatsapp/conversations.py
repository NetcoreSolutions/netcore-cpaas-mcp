"""WhatsApp Conversation APIs — send messages within 24h customer conversation window."""

from netcore_whatsapp import BASE_URL, api_post


# ---------------------------------------------------------------------------
# Send Conversation Message (v3)
# ---------------------------------------------------------------------------
def send_conversation_message(message_data: dict) -> dict:
    """Send a WhatsApp conversation message (text, media, interactive, etc.).

    Supports text, image, video, audio, document, sticker, location, contacts,
    and interactive messages (buttons, lists, flows, catalogs).

    Args:
        message_data: Dict with 'to' (recipient WhatsApp ID), 'type' (message type),
            and the corresponding type object (text, image, interactive, etc.).
    """
    url = f"{BASE_URL}/v3/metainfo/messages"
    return api_post(url, json_data=message_data)
