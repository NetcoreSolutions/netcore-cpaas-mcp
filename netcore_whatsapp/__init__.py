import os
import requests
import traceback
from dotenv import load_dotenv

load_dotenv()

WHATSAPP_TOKEN = os.getenv('WHATSAPP_TOKEN')

BASE_URL = "https://cpaaswa.netcorecloud.net/api"
MEDIA_BASE_URL = "https://waapi.pepipost.com/api/v2"
MISC_BASE_URL = "https://cpaaswa.netcorecloud.net"
CONSENT_BASE_URL = "https://cpaaswa.netcorecloud.net/api/v2/consent"
PAYMENT_BASE_URL = "https://cpaaswa.netcorecloud.net/api/v2"


def get_headers(content_type="application/json"):
    """Return common headers for API requests."""
    headers = {
        'Authorization': WHATSAPP_TOKEN,
    }
    if content_type:
        headers['Content-Type'] = content_type
    return headers


def api_get(url, params=None, headers=None):
    """Perform a GET request and return parsed JSON or None on error."""
    if headers is None:
        headers = get_headers()
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        content_type = response.headers.get('Content-Type', '')
        if 'application/json' in content_type:
            return response.json()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"API GET error ({url}): {str(e)}")
        traceback.print_exc()
        return None


def api_post(url, json_data=None, headers=None):
    """Perform a POST request with JSON body and return parsed JSON or None on error."""
    if headers is None:
        headers = get_headers()
    try:
        response = requests.post(url, headers=headers, json=json_data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API POST error ({url}): {str(e)}")
        traceback.print_exc()
        return None


def api_put(url, json_data=None, headers=None):
    """Perform a PUT request with JSON body and return parsed JSON or None on error."""
    if headers is None:
        headers = get_headers()
    try:
        response = requests.put(url, headers=headers, json=json_data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API PUT error ({url}): {str(e)}")
        traceback.print_exc()
        return None


def api_delete(url, params=None, headers=None):
    """Perform a DELETE request and return parsed JSON or None on error."""
    if headers is None:
        headers = get_headers()
    try:
        response = requests.delete(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API DELETE error ({url}): {str(e)}")
        traceback.print_exc()
        return None


def api_post_multipart(url, files=None, data=None, headers=None):
    """Perform a POST request with multipart/form-data and return parsed JSON or None on error."""
    if headers is None:
        headers = {'Authorization': WHATSAPP_TOKEN}
    try:
        response = requests.post(url, headers=headers, files=files, data=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API POST multipart error ({url}): {str(e)}")
        traceback.print_exc()
        return None


# Re-export all integration functions
from netcore_whatsapp.templates import *
from netcore_whatsapp.messaging import *
from netcore_whatsapp.media import *
from netcore_whatsapp.consent import *
from netcore_whatsapp.flows import *
from netcore_whatsapp.analytics import *
from netcore_whatsapp.conversations import *
from netcore_whatsapp.conversions import *
from netcore_whatsapp.payments import *
from netcore_whatsapp.webhooks import *
from netcore_whatsapp.misc import *
