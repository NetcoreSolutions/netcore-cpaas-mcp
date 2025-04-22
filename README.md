cd cpaas-mcp
uv venv

# Mac/Linux:
uv venv
source .venv/bin/activate

# Windows:
.venv\Scripts\activate

# Install the required dependencies:
uv add "mcp[cli]" requests python-dotenv

# Next, set up your environment variables in a .env file:
WHATSAPP_TOKEN=your_netcore_cpaas_whatsapp_token

curl --location 'http://waapi.pepipost.com/api/v2/metainfo/template/status?templatename=rk_lines' \
--header 'Authorization: <WHATSAPP_TOKEN>'


/Users/vishal.v/Library/Application\ Support/Claude/claude_desktop_config.json

```
{
    "mcpServers": {
        "netcore-cpaas-whatsapp": {
            "command": "/Users/vishal.v/dev/netcore/netcore-cpaas-mcp/.venv/bin/python",
            "args": [
                "/Users/vishal.v/dev/netcore/netcore-cpaas-mcp/netcore_cpaas_mcp.py",
                "--debug"
            ],
            "env": {
                "WHATSAPP_TOKEN": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJrYXZpdGFzaGluZGUxMTVsbm5jcWZ8OTg2NzY0NDY3MyIsImV4cCI6MjU2Njk4NTc5OX0.uxxL3e_v51LTyjQjBu662gxWfW1_equlYytErq4wMGpAEDGXna7V0NxY6uI3UwC-kgfMz4Yh6JBwo_op-911mA"
            }
        }
    }
}
```