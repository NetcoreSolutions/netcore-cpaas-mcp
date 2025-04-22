# NETCORE CPaaS MCP Server

A Message Control Protocol (MCP) server implementation for NETCORE CPaaS channels, currently supporting WhatsApp integration with plans to support RCS, SMS, and Email channels.

## Overview

This MCP server provides a standardized interface for interacting with NETCORE CPaaS services, currently focusing on WhatsApp messaging capabilities. The server implements various tools for template management and message sending.

## Features

### WhatsApp Integration
- Template Status Checking
- Template Preview Retrieval
- Template Message Sending

## Prerequisites

- Python 3.x
- NETCORE CPaaS WhatsApp API credentials
- MCP CLI tools

## Installation

1: Install the uv package manager

```bash
# For Mac/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# For Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

2. Clone the repository:

```bash
git clone <repository-url>
cd netcore-cpaas-mcp
```

3. Create and activate a virtual environment:

```bash
# Mac/Linux:
uv venv
source .venv/bin/activate

# Windows:
.venv\Scripts\activate
```

4. Install dependencies:
```bash
uv add "mcp[cli]" requests python-dotenv
uv pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in the project root with the following content:
```
WHATSAPP_TOKEN=your_netcore_cpaas_whatsapp_token
```

2. Configure MCP server in your MCP client configuration e.g. Claude Desktop or Cursor IDE:
```json
{
    "mcpServers": {
        "netcore-cpaas-whatsapp": {
            "command": "path/to/python",
            "args": [
                "path/to/netcore_cpaas_mcp.py",
                "--debug"
            ],
            "env": {
                "WHATSAPP_TOKEN": "your_whatsapp_token"
            }
        }
    }
}
```

## Available Tools

### WhatsApp Tools

1. **get_template_status**
   - Description: Fetches the status of a WhatsApp template
   - Parameters:
     - `template_name`: Name of the template to check
   - Returns: Template status information

2. **get_template_preview**
   - Description: Retrieves preview information for a WhatsApp template
   - Parameters:
     - `template_name`: Name of the template to preview
   - Returns: Template preview details

3. **send_whatsapp_template**
   - Description: Sends a WhatsApp template message to a recipient
   - Parameters:
     - `template_name`: Name of the template to use
     - `recipient_whatsapp`: Recipient's WhatsApp number
   - Returns: API response containing message status

## Development

The project is structured as follows:
- `netcore_cpaas_mcp.py`: Main MCP server implementation
- `netcore_whatsapp_integration.py`: WhatsApp-specific integration code
- `requirements.txt`: Project dependencies

## Future Enhancements

- RCS channel integration
- SMS channel integration
- Email channel integration
- Enhanced error handling and logging
- Additional template management features

## Support

For support or questions, please contact the development team.

## License

[Add your license information here]
