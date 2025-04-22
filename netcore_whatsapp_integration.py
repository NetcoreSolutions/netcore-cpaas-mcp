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

# Example usage for debugging
# status = fetch_template_status('rk_lines')
# print(status)