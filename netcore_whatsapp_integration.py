import os
import requests
import traceback
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
WHATSAPP_TOKEN = os.getenv('WHATSAPP_TOKEN')
BASE_URL = "http://waapi.pepipost.com/api/v2"

def fetch_template_status(template_name: str) -> dict:
    """Fetch the status of a WhatsApp template.
    
    Args:
        template_name: The name of the template to check status for
        
    Returns:
        A dictionary containing the template status information
    """
    url = f"{BASE_URL}/metainfo/template/status?templatename={template_name}"
    headers = {
        'Authorization': WHATSAPP_TOKEN
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching template status: {str(e)}")
        traceback.print_exc()
        return None

def fetch_template_preview(template_name: str) -> dict:
    """Fetch the preview or details of a WhatsApp template.
    
    Args:
        template_name: The name of the template to get preview/details for
        
    Returns:
        A dictionary containing the template preview information
    """
    url = f"{BASE_URL}/metainfo/template/preview?templatename={template_name}"
    headers = {
        'Authorization': WHATSAPP_TOKEN
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching template preview: {str(e)}")
        traceback.print_exc()
        return None

def send_template_message(template_name: str, recipient_whatsapp: str) -> dict:
    """Send a WhatsApp template message to a recipient.
    
    Args:
        template_name: The name of the template to use
        recipient_whatsapp: The recipient's WhatsApp number
        
    Returns:
        A dictionary containing the API response
    """
    url = f"{BASE_URL}/message/nc/priority"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': WHATSAPP_TOKEN
    }
    
    payload = {
        "message": [
            {
                "recipient_whatsapp": recipient_whatsapp,
                "cta_link_track": 1,
                "message_type": "template",
                "source": "",
                "x-apiheader": "",
                "recipient_type": "individual",
                "type_template": [
                    {
                        "name": template_name,
                        "attributes": [
                            "https://www.google.com"  # This could be made configurable if needed
                        ],
                        "language": {
                            "locale": "en",
                            "policy": "deterministic"
                        }
                    }
                ]
            }
        ]
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error sending template message: {str(e)}")
        traceback.print_exc()
        return None

def create_template(template_data: dict) -> dict:
    """Create a new WhatsApp template.
    
    Args:
        template_data: Dictionary containing template details including:
            - category: Template category (e.g., "MARKETING")
            - name: Template name
            - language: Template language code (e.g., "en_US")
            - allow_category_change: Boolean to allow category changes
            - components: List of template components (header, body, footer, buttons)
        
    Returns:
        A dictionary containing the API response
    """
    url = f"{BASE_URL}/metainfo/template/create"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': WHATSAPP_TOKEN
    }
    
    try:
        response = requests.post(url, headers=headers, json=template_data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error creating template: {str(e)}")
        traceback.print_exc()
        return None

# Example usage for debugging

# status = fetch_template_status('rk_lines')
# print(status)

templateData = fetch_template_preview('rk_lines')
print(templateData)