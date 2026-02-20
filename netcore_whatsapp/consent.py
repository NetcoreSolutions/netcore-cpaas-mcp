"""WhatsApp Consent Management APIs — opt-in/out, blocklist/whitelist."""

from netcore_whatsapp import CONSENT_BASE_URL, api_post


# ---------------------------------------------------------------------------
# Manage User Consent (Opt-in / Opt-out)
# ---------------------------------------------------------------------------
def manage_user_consent(consent_data: dict) -> dict:
    """Register or update user consent for WhatsApp messaging.

    Args:
        consent_data: Dict with 'type' ("optin" or "optout") and 'recipients' array.
            Each recipient has: recipient (phone), source, user_agent, ip.
    """
    url = f"{CONSENT_BASE_URL}/manage"
    return api_post(url, json_data=consent_data)


# ---------------------------------------------------------------------------
# Manage Blocklist / Whitelist
# ---------------------------------------------------------------------------
def manage_blocklist(blocklist_data: dict) -> dict:
    """Add or remove phone numbers from the blocklist or whitelist.

    Args:
        blocklist_data: Dict with 'type' ("blocklist" or "whitelist") and 'recipients' array.
            Each recipient has: recipient (phone), source, user_agent, ip.
    """
    url = f"{CONSENT_BASE_URL}/blocklist"
    return api_post(url, json_data=blocklist_data)
