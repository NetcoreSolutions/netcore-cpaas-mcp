"""WhatsApp Flows APIs — list, create, publish, delete, deprecate, edit, preview."""

from netcore_whatsapp import BASE_URL, api_get, api_post, api_delete, api_post_multipart, get_headers
import requests
import traceback


# ---------------------------------------------------------------------------
# Fetch Flow List (v3)
# ---------------------------------------------------------------------------
def fetch_flow_list(pagination_token: str = None) -> dict:
    """Retrieve a list of WhatsApp Flows for the WABA.

    Args:
        pagination_token: Optional token for fetching the next page of results.
    """
    url = f"{BASE_URL}/v3/metainfo/flow/list"
    params = {}
    if pagination_token:
        params["pagination_token"] = pagination_token
    return api_get(url, params=params)


# ---------------------------------------------------------------------------
# Create Flow (v3)
# ---------------------------------------------------------------------------
def create_flow(flow_data: dict) -> dict:
    """Create a new interactive WhatsApp Flow.

    Args:
        flow_data: Dict with 'name', 'categories' (array), 'flow_json' (string),
            and optionally 'publish' (bool).
    """
    url = f"{BASE_URL}/v3/metainfo/flow/create"
    return api_post(url, json_data=flow_data)


# ---------------------------------------------------------------------------
# Publish Flow (v3)
# ---------------------------------------------------------------------------
def publish_flow(flow_id: str) -> dict:
    """Publish an existing WhatsApp flow, making it live.

    Args:
        flow_id: The unique ID of the flow to publish.
    """
    url = f"{BASE_URL}/v3/metainfo/flow/publish"
    return api_get(url, params={"flowid": flow_id})


# ---------------------------------------------------------------------------
# Delete Flow (v3)
# ---------------------------------------------------------------------------
def delete_flow(flow_id: str) -> dict:
    """Delete an unpublished WhatsApp flow.

    Args:
        flow_id: The unique ID of the flow to delete.
    """
    url = f"{BASE_URL}/v3/metainfo/flow/delete"
    return api_delete(url, params={"flowid": flow_id})


# ---------------------------------------------------------------------------
# Deprecate Flow (v3)
# ---------------------------------------------------------------------------
def deprecate_flow(flow_id: str) -> dict:
    """Deprecate a published WhatsApp flow, marking it inactive.

    Args:
        flow_id: The unique ID of the flow to deprecate.
    """
    url = f"{BASE_URL}/v3/metainfo/flow/deprecate"
    headers = get_headers()
    try:
        response = requests.post(url, headers=headers, params={"flowid": flow_id})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error deprecating flow: {str(e)}")
        traceback.print_exc()
        return None


# ---------------------------------------------------------------------------
# Edit Flow Metadata (v3)
# ---------------------------------------------------------------------------
def edit_flow_metadata(flow_id: str, metadata: dict) -> dict:
    """Update metadata fields (name, categories) of an existing flow.

    Args:
        flow_id: The unique ID of the flow.
        metadata: Dict with optional 'name' and 'categories' fields.
    """
    url = f"{BASE_URL}/v3/metainfo/flow/edit/metadata"
    headers = get_headers()
    try:
        response = requests.post(
            url, headers=headers, params={"flowid": flow_id}, json=metadata
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error editing flow metadata: {str(e)}")
        traceback.print_exc()
        return None


# ---------------------------------------------------------------------------
# Get Flow Preview URL (v3)
# ---------------------------------------------------------------------------
def fetch_flow_preview(flow_id: str) -> dict:
    """Generate a preview URL for a WhatsApp Flow.

    Args:
        flow_id: The unique ID of the flow to preview.
    """
    url = f"{BASE_URL}/v3/metainfo/flow/preview"
    return api_get(url, params={"flow_id": flow_id})
