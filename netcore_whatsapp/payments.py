"""WhatsApp Payment APIs — status, refund, OAuth link, configuration CRUD."""

from netcore_whatsapp import PAYMENT_BASE_URL, api_get, api_post, api_delete


# ---------------------------------------------------------------------------
# Get Payment Status
# ---------------------------------------------------------------------------
def fetch_payment_status(payment_configuration: str, reference_id: str) -> dict:
    """Retrieve the current status of a payment transaction.

    Args:
        payment_configuration: Name of the configured payment setup.
        reference_id: Unique ID of the payment transaction.
    """
    url = f"{PAYMENT_BASE_URL}/payments/status/{payment_configuration}/{reference_id}"
    return api_get(url)


# ---------------------------------------------------------------------------
# Process Payment Refund
# ---------------------------------------------------------------------------
def process_refund(refund_data: dict) -> dict:
    """Initiate a refund for a completed transaction.

    Args:
        refund_data: Dict with reference_id, speed ("normal"/"instant"),
            payment_config_id, and amount (currency, value, offset).
    """
    url = f"{PAYMENT_BASE_URL}/payments/refund/payments_refund"
    return api_post(url, json_data=refund_data)


# ---------------------------------------------------------------------------
# Generate OAuth Link for Payment Configuration
# ---------------------------------------------------------------------------
def create_oauth_link(oauth_data: dict) -> dict:
    """Generate an OAuth link for payment gateway configuration.

    Args:
        oauth_data: Dict with 'configuration_name' and 'redirect_url'.
    """
    url = f"{PAYMENT_BASE_URL}/v2/payments/configuration/oauth_link"
    return api_post(url, json_data=oauth_data)


# ---------------------------------------------------------------------------
# Create Payment Configuration
# ---------------------------------------------------------------------------
def create_payment_configuration(config_data: dict) -> dict:
    """Create a new payment gateway configuration.

    Args:
        config_data: Dict with configuration_name, provider_name, redirect_url,
            merchant_category_code, and purpose_code.
    """
    url = f"{PAYMENT_BASE_URL}/v2/payments/configuration"
    return api_post(url, json_data=config_data)


# ---------------------------------------------------------------------------
# Delete Payment Configuration
# ---------------------------------------------------------------------------
def delete_payment_configuration(configuration_name: str) -> dict:
    """Delete a payment gateway configuration by name.

    Args:
        configuration_name: Name of the payment configuration to delete.
    """
    url = f"{PAYMENT_BASE_URL}/v2/payments/configuration/{configuration_name}"
    return api_delete(url)
