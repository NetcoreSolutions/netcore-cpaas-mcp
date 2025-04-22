import sys
import os
import traceback
import argparse
from typing import Any, List, Dict
from mcp.server.fastmcp import FastMCP
from netcore_whatsapp_integration import fetch_template_status, fetch_template_preview, send_template_message, create_template, fetch_media_details, fetch_template_list
from dotenv import load_dotenv

class NetcoreCPaaSMCP:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        # Initialize MCP Server
        self.mcp = FastMCP("netcore_cpaas_mcp")
        print("MCP Server initialized", file=sys.stderr)
        
        # Register MCP tools
        self._register_tools()
    
    def _register_tools(self):
        """Register Netcore MCP tools for Netcore Whatsapp Integration."""
        
        @self.mcp.tool()
        async def get_template_status(template_name: str) -> Dict[str, Any]:
            """Fetch the status of a WhatsApp template.
            
            Args:
                template_name: The name of the template to check status for
                
            Returns:
                A dictionary containing the template status information
            """
            print(f"Fetching status for template: {template_name}", file=sys.stderr)
            try:
                status = fetch_template_status(template_name)
                if status is None:
                    print(f"No status returned for template: {template_name}", file=sys.stderr)
                    return {}
                
                print(f"Successfully fetched template status", file=sys.stderr)
                return status
            except Exception as e:
                print(f"Error fetching template status: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        @self.mcp.tool()
        async def get_template_preview(template_name: str) -> Dict[str, Any]:
            """Fetch the preview of a WhatsApp template.
            
            Args:
                template_name: The name of the template to get preview for
                
            Returns:
                A dictionary containing the template preview information
            """
            print(f"Fetching preview for template: {template_name}", file=sys.stderr)
            try:
                preview = fetch_template_preview(template_name)
                if preview is None:
                    print(f"No preview returned for template: {template_name}", file=sys.stderr)
                    return {}
                
                print(f"Successfully fetched template preview", file=sys.stderr)
                return preview
            except Exception as e:
                print(f"Error fetching template preview: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        @self.mcp.tool()
        async def send_whatsapp_template(template_name: str, recipient_whatsapp: str) -> Dict[str, Any]:
            """Send a WhatsApp template message to a recipient.
            
            Args:
                template_name: The name of the template to use
                recipient_whatsapp: The recipient's WhatsApp number
                
            Returns:
                A dictionary containing the API response
            """
            print(f"Sending template '{template_name}' to {recipient_whatsapp}", file=sys.stderr)
            try:
                response = send_template_message(template_name, recipient_whatsapp)
                if response is None:
                    print(f"Failed to send template message", file=sys.stderr)
                    return {}
                
                print(f"Successfully sent template message", file=sys.stderr)
                return response
            except Exception as e:
                print(f"Error sending template message: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        @self.mcp.tool()
        async def create_whatsapp_template(template_data: Dict[str, Any]) -> Dict[str, Any]:
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
            print(f"Creating new WhatsApp template: {template_data.get('name')}", file=sys.stderr)
            try:
                response = create_template(template_data)
                if response is None:
                    print(f"Failed to create template", file=sys.stderr)
                    return {}
                
                print(f"Successfully created template", file=sys.stderr)
                return response
            except Exception as e:
                print(f"Error creating template: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        @self.mcp.tool()
        async def get_media_details(media_id: str) -> Dict[str, Any]:
            """Fetch the preview or details of a WhatsApp media.
            
            Args:
                media_id: The ID of the media to get preview/details for
                
            Returns:
                A dictionary containing the media details information
            """
            print(f"Fetching details for media: {media_id}", file=sys.stderr)
            try:
                details = fetch_media_details(media_id)
                if details is None:
                    print(f"No details returned for media: {media_id}", file=sys.stderr)
                    return {}
                
                print(f"Successfully fetched media details", file=sys.stderr)
                return details
            except Exception as e:
                print(f"Error fetching media details: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        @self.mcp.tool()
        async def get_template_list(limit: int = 10, offset: int = 0, status: str = "Approved", language: str = "English", template_type: str = "1,2") -> Dict[str, Any]:
            """Fetch the list of WhatsApp templates with optional filters.
            
            Args:
                limit: Maximum number of templates to return (default: 10)
                offset: Number of templates to skip (default: 0)
                status: Filter by template status (default: "Approved")
                language: Filter by template language (default: "English")
                template_type: Filter by template types (default: "1,2")
                
            Returns:
                A dictionary containing the list of templates
            """
            print(f"Fetching template list with filters: limit={limit}, offset={offset}, status={status}, language={language}, template_type={template_type}", file=sys.stderr)
            try:
                templates = fetch_template_list(limit, offset, status, language, template_type)
                if templates is None:
                    print(f"No templates returned", file=sys.stderr)
                    return {}
                
                print(f"Successfully fetched template list", file=sys.stderr)
                return templates
            except Exception as e:
                print(f"Error fetching template list: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}
    
    def run(self):
        """Start the MCP server."""
        try:
            print("Running Netcore CPaaS MCP Server...", file=sys.stderr)
            self.mcp.run(transport="stdio")
        except Exception as e:
            print(f"Fatal Error in MCP Server: {str(e)}", file=sys.stderr)
            traceback.print_exc(file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Netcore CPaaS MCP Server')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    args = parser.parse_args()
    
    if args.debug:
        print("Debug mode enabled", file=sys.stderr)
    
    try:
        analyzer = NetcoreCPaaSMCP()
        analyzer.run()
    except Exception as e:
        print(f"Failed to start MCP server: {str(e)}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)