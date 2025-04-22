cd cpaas-mcp
uv venv

# Mac/Linux:
uv venv
source .venv/bin/activate

# Windows:
.venv\Scripts\activate

# Install the required dependencies:
uv add "mcp[cli]" requests python-dotenv

# Install these dependencies:
uv pip install -r requirements.txt

# Next, set up your environment variables in a .env file:
WHATSAPP_TOKEN=your_netcore_cpaas_whatsapp_token

Template Names:
rk_lines, doc_cta

curl --location 'http://waapi.pepipost.com/api/v2/metainfo/template/status?templatename=rk_lines' \
--header 'Authorization: <WHATSAPP_TOKEN>'

curl --location 'https://waapi.pepipost.com/api/v2/metainfo/template/preview?templatename=doc_cta' \
--header 'Authorization: <WHATSAPP_TOKEN>' \

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
                "WHATSAPP_TOKEN": "<AUTH_TOKEN>"
            }
        }
    }
}
```


curl --location 'https://cpaaswa.netcorecloud.net/api/v2/message/nc/priority' \
--header 'Content-Type: application/json' \
--header '<WHATSAPP_TOKEN>' \
--data '{
    "message": [
        {
            "recipient_whatsapp": "",
            "cta_link_track": 1,
            "message_type": "template",
            "source": "",
            "x-apiheader": "",
            "recipient_type": "individual",
            "type_template": [
                {
                    "name": "test_template_eu",
                    "attributes": [
                        "https://www.google.com"
                    ],
                    "language": {
                        "locale": "en",
                        "policy": "deterministic"
                    }
                }
            ]
        }
    ]
}'