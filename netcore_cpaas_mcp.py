import sys
import os
import traceback
import argparse
from typing import Any, List, Dict
from mcp.server.fastmcp import FastMCP
from netcore_whatsapp_integration import fetch_template_status
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