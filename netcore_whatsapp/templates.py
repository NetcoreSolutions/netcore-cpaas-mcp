"""WhatsApp Template management APIs — list, create, edit, delete, preview, status, etc."""

from netcore_whatsapp import BASE_URL, api_get, api_post, api_put, get_headers


# ---------------------------------------------------------------------------
# Template List (v3)
# ---------------------------------------------------------------------------
def fetch_template_list(
    limit: int = 10,
    offset: int = 0,
    status: str = None,
    template_name: str = None,
    language: str = None,
    template_type: str = None,
) -> dict:
    """Retrieve a paginated list of WhatsApp templates with optional filters.

    Args:
        limit: Maximum number of templates to return.
        offset: Number of records to skip for pagination.
        status: Filter by approval status (approved, rejected, pending).
        template_name: Filter by partial or full template name.
        language: Filter by language (e.g. English, Hindi).
        template_type: Filter by type (comma-separated, e.g. "1,2").
    """
    url = f"{BASE_URL}/v3/metainfo/template/list"
    params = {"limit": limit, "offset": offset}
    if status:
        params["status"] = status
    if template_name:
        params["template_name"] = template_name
    if language:
        params["language"] = language
    if template_type:
        params["template_type"] = template_type
    return api_get(url, params=params)


# ---------------------------------------------------------------------------
# Template Create (v3)
# ---------------------------------------------------------------------------
def create_template(template_data: dict) -> dict:
    """Create a new WhatsApp template.

    Args:
        template_data: Dictionary with meta_payload and optional nc_payload.
            meta_payload must include name, language, category, and components.
    """
    url = f"{BASE_URL}/v3/metainfo/template/create"
    return api_post(url, json_data=template_data)


# ---------------------------------------------------------------------------
# Template Edit (v3)
# ---------------------------------------------------------------------------
def edit_template(template_data: dict) -> dict:
    """Edit an existing WhatsApp template.

    Args:
        template_data: Dictionary with meta_payload (same structure as create).
    """
    url = f"{BASE_URL}/v3/metainfo/template/edit"
    return api_put(url, json_data=template_data)


# ---------------------------------------------------------------------------
# Template Delete (v3)
# ---------------------------------------------------------------------------
def delete_template(name: str, language: str) -> dict:
    """Delete a WhatsApp template by name and language.

    Args:
        name: Template name to delete.
        language: Template language code.
    """
    url = f"{BASE_URL}/v3/metainfo/template/delete"
    return api_post(url, json_data={"name": name, "language": language})


# ---------------------------------------------------------------------------
# Template Preview (v3)
# ---------------------------------------------------------------------------
def fetch_template_preview(
    template_name: str = None, template_id: int = None
) -> dict:
    """Preview a WhatsApp template to see how it will look.

    Args:
        template_name: Name of the template to preview.
        template_id: Numeric ID of the template to preview.
    """
    url = f"{BASE_URL}/v3/metainfo/template/preview"
    params = {}
    if template_name:
        params["templatename"] = template_name
    if template_id:
        params["templateid"] = template_id
    return api_get(url, params=params)


# ---------------------------------------------------------------------------
# Template Status (v3)
# ---------------------------------------------------------------------------
def fetch_template_status(
    template_name: str = None, template_id: int = None
) -> dict:
    """Get the approval status of a WhatsApp template.

    Args:
        template_name: Name of the template.
        template_id: Numeric ID of the template.
    """
    url = f"{BASE_URL}/v3/metainfo/template/status"
    params = {}
    if template_name:
        params["templatename"] = template_name
    if template_id:
        params["templateid"] = template_id
    return api_get(url, params=params)


# ---------------------------------------------------------------------------
# Category List (v3)
# ---------------------------------------------------------------------------
def fetch_template_category_list() -> dict:
    """Get the list of all available template categories."""
    url = f"{BASE_URL}/v3/metainfo/template/categorylist"
    return api_get(url)


# ---------------------------------------------------------------------------
# Language List (v3)
# ---------------------------------------------------------------------------
def fetch_template_language_list() -> dict:
    """Get the list of all available template languages."""
    url = f"{BASE_URL}/v3/metainfo/template/languagelist"
    return api_get(url)


# ---------------------------------------------------------------------------
# Display Number Details (v3)
# ---------------------------------------------------------------------------
def fetch_display_number_details() -> dict:
    """Get display number details including verification status, quality rating, and messaging limit."""
    url = f"{BASE_URL}/v3/metainfo/template/display_number_details"
    return api_get(url)


# ---------------------------------------------------------------------------
# Template Profile Details (v3)
# ---------------------------------------------------------------------------
def fetch_template_profile_details() -> dict:
    """Get the profile details (client name and profile image) for templates."""
    url = f"{BASE_URL}/v3/metainfo/template/profiledetails"
    return api_get(url)


# ---------------------------------------------------------------------------
# Edit Template Category (v3)
# ---------------------------------------------------------------------------
def edit_template_category(
    new_category: str,
    template_id: int = None,
    template_name: str = None,
    stop_at_cc: bool = False,
    template_save_mode: str = "draft",
) -> dict:
    """Change the category of an existing template.

    Args:
        new_category: New category (Marketing, Utility, Authentication).
        template_id: Numeric template ID.
        template_name: Template name.
        stop_at_cc: Whether to stop at content creation stage.
        template_save_mode: Save mode — 'draft' or 'publish'.
    """
    url = f"{BASE_URL}/v3/metainfo/template/edit_category"
    params = {}
    if template_id:
        params["template_id"] = template_id
    if template_name:
        params["template_name"] = template_name
    payload = {
        "new_category": new_category,
        "stop_at_cc": stop_at_cc,
        "template_save_mode": template_save_mode,
    }
    headers = get_headers()
    import requests
    try:
        response = requests.post(url, headers=headers, params=params, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        import traceback
        print(f"Error editing template category: {str(e)}")
        traceback.print_exc()
        return None
