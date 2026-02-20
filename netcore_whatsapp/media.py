"""WhatsApp Media APIs — upload media, get media, create media handler."""

from netcore_whatsapp import BASE_URL, MEDIA_BASE_URL, api_get, api_post_multipart, WHATSAPP_TOKEN


# ---------------------------------------------------------------------------
# Get Media File (v2)
# ---------------------------------------------------------------------------
def fetch_media_details(media_id: str) -> dict:
    """Retrieve a media file or its details using its media ID.

    Args:
        media_id: Unique identifier of the media file.
    """
    url = f"{MEDIA_BASE_URL}/media/{media_id}"
    return api_get(url)


# ---------------------------------------------------------------------------
# Upload Media File (v2)
# ---------------------------------------------------------------------------
def upload_media(file_path: str) -> dict:
    """Upload a media file (image, video, document) and get a media ID.

    Args:
        file_path: Local path to the media file to upload.
    """
    url = f"{MEDIA_BASE_URL}/media/upload"
    with open(file_path, 'rb') as f:
        files = {'file': f}
        return api_post_multipart(url, files=files)


# ---------------------------------------------------------------------------
# Create Media Handler for Templates (v3)
# ---------------------------------------------------------------------------
def create_media_handler(file_path: str, media_format: str) -> dict:
    """Upload a media file and create a handler ID for use in WhatsApp templates.

    Args:
        file_path: Local path to the media file (image, video, or document).
        media_format: Media type — 'image', 'video', or 'document'.
    """
    url = f"{BASE_URL}/v3/metainfo/template/create_media_handler"
    with open(file_path, 'rb') as f:
        files = {'file': f}
        data = {'format': media_format}
        return api_post_multipart(url, files=files, data=data)
