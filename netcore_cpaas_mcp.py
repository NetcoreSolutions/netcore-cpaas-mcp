import sys
import os
import traceback
import argparse
from typing import Any, List, Dict, Optional
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

# Import all integration functions from the netcore_whatsapp package
from netcore_whatsapp.templates import (
    fetch_template_list,
    create_template,
    edit_template,
    delete_template,
    fetch_template_preview,
    fetch_template_status,
    fetch_template_category_list,
    fetch_template_language_list,
    fetch_display_number_details,
    fetch_template_profile_details,
    edit_template_category,
)
from netcore_whatsapp.messaging import (
    send_template_message,
)
from netcore_whatsapp.media import (
    fetch_media_details,
    upload_media,
    create_media_handler,
)
from netcore_whatsapp.consent import (
    manage_user_consent,
    manage_blocklist,
)
from netcore_whatsapp.flows import (
    fetch_flow_list,
    create_flow,
    publish_flow,
    delete_flow,
    deprecate_flow,
    edit_flow_metadata,
    fetch_flow_preview,
)
from netcore_whatsapp.analytics import (
    fetch_template_analytics,
)
from netcore_whatsapp.conversations import (
    send_conversation_message,
)
from netcore_whatsapp.conversions import (
    track_conversions,
)
from netcore_whatsapp.payments import (
    fetch_payment_status,
    process_refund,
    create_oauth_link,
    create_payment_configuration,
    delete_payment_configuration,
)
from netcore_whatsapp.webhooks import (
    fetch_webhook_list,
    update_webhook,
    manage_webhook_status,
)
from netcore_whatsapp.misc import (
    fetch_whatsapp_settings,
    fetch_whatsapp_stats,
    fetch_whatsapp_messages,
    fetch_summary_stats,
)


class NetcoreCPaaSMCP:
    def __init__(self):
        load_dotenv()
        self.mcp = FastMCP("netcore_cpaas_mcp")
        print("MCP Server initialized", file=sys.stderr)
        self._register_tools()

    # ===================================================================
    # TOOL REGISTRATION
    # ===================================================================
    def _register_tools(self):
        """Register all Netcore WhatsApp MCP tools."""

        # ---------------------------------------------------------------
        # 1. TEMPLATE TOOLS
        # ---------------------------------------------------------------

        @self.mcp.tool()
        async def get_template_list(
            limit: int = 10,
            offset: int = 0,
            status: str = None,
            template_name: str = None,
            language: str = None,
            template_type: str = None,
        ) -> Dict[str, Any]:
            """Fetch a paginated list of WhatsApp templates with optional filters.

            Args:
                limit: Maximum number of templates to return (default: 10)
                offset: Number of records to skip for pagination (default: 0)
                status: Filter by approval status (approved, rejected, pending)
                template_name: Filter by partial or full template name
                language: Filter by language (e.g. English, Hindi)
                template_type: Filter by type (comma-separated, e.g. "1,2")

            Returns:
                A dictionary containing the list of templates with pagination info
            """
            print(f"Fetching template list", file=sys.stderr)
            try:
                result = fetch_template_list(limit, offset, status, template_name, language, template_type)
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        @self.mcp.tool()
        async def create_whatsapp_template(template_data: Dict[str, Any]) -> Dict[str, Any]:
            """Create a new WhatsApp template (text, media, carousel, LTO, SPM, order, etc.).

            Args:
                template_data: Dictionary containing template details with meta_payload including:
                    - name: Template name
                    - language: Language code (e.g., "en")
                    - category: Category (MARKETING, UTILITY, AUTHENTICATION)
                    - components: List of template components (HEADER, BODY, FOOTER, BUTTONS)
                    And optional nc_payload.

            Returns:
                A dictionary containing the API response with template_id and status
            """
            print(f"Creating template: {template_data.get('meta_payload', {}).get('name', 'unknown')}", file=sys.stderr)
            try:
                result = create_template(template_data)
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        @self.mcp.tool()
        async def edit_whatsapp_template(template_data: Dict[str, Any]) -> Dict[str, Any]:
            """Edit an existing WhatsApp template.

            Args:
                template_data: Dictionary with meta_payload (same structure as create) including
                    name, language, category, and components to update.

            Returns:
                A dictionary containing the API response
            """
            print(f"Editing template: {template_data.get('meta_payload', {}).get('name', 'unknown')}", file=sys.stderr)
            try:
                result = edit_template(template_data)
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        @self.mcp.tool()
        async def delete_whatsapp_template(name: str, language: str) -> Dict[str, Any]:
            """Delete a WhatsApp template by name and language.

            Args:
                name: The name of the template to delete
                language: The language code of the template to delete

            Returns:
                A dictionary indicating success or failure
            """
            print(f"Deleting template: {name} ({language})", file=sys.stderr)
            try:
                result = delete_template(name, language)
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        @self.mcp.tool()
        async def get_template_preview(template_name: str = None, template_id: int = None) -> Dict[str, Any]:
            """Preview a WhatsApp template to see how it will look before sending.

            Args:
                template_name: Name of the template to preview
                template_id: Numeric ID of the template to preview

            Returns:
                A dictionary containing the template preview information
            """
            print(f"Fetching template preview: {template_name or template_id}", file=sys.stderr)
            try:
                result = fetch_template_preview(template_name, template_id)
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        @self.mcp.tool()
        async def get_template_status(template_name: str = None, template_id: int = None) -> Dict[str, Any]:
            """Fetch the approval status of a WhatsApp template.

            Args:
                template_name: Name of the template to check status for
                template_id: Numeric ID of the template to check status for

            Returns:
                A dictionary containing the template status information
            """
            print(f"Fetching template status: {template_name or template_id}", file=sys.stderr)
            try:
                result = fetch_template_status(template_name, template_id)
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        @self.mcp.tool()
        async def get_template_category_list() -> Dict[str, Any]:
            """Get the list of all available WhatsApp template categories (Marketing, Utility, Authentication).

            Returns:
                A dictionary containing the list of template categories
            """
            print("Fetching template category list", file=sys.stderr)
            try:
                result = fetch_template_category_list()
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        @self.mcp.tool()
        async def get_template_language_list() -> Dict[str, Any]:
            """Get the list of all available WhatsApp template languages.

            Returns:
                A dictionary containing the list of supported template languages
            """
            print("Fetching template language list", file=sys.stderr)
            try:
                result = fetch_template_language_list()
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        @self.mcp.tool()
        async def get_display_number_details() -> Dict[str, Any]:
            """Get display number details including verification status, quality rating, and messaging limit.

            Returns:
                A dictionary with verified status, quality_rating, messaging_limit,
                whatsapp_number, business_name, and business_profile_logo
            """
            print("Fetching display number details", file=sys.stderr)
            try:
                result = fetch_display_number_details()
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        @self.mcp.tool()
        async def get_template_profile_details() -> Dict[str, Any]:
            """Get the business profile details (client name and profile image) for templates.

            Returns:
                A dictionary with client_name and client_profile_url
            """
            print("Fetching template profile details", file=sys.stderr)
            try:
                result = fetch_template_profile_details()
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        @self.mcp.tool()
        async def edit_whatsapp_template_category(
            new_category: str,
            template_id: int = None,
            template_name: str = None,
            stop_at_cc: bool = False,
            template_save_mode: str = "draft",
        ) -> Dict[str, Any]:
            """Change the category of an existing WhatsApp template.

            Args:
                new_category: New category — "Marketing", "Utility", or "Authentication"
                template_id: Numeric template ID (provide this or template_name)
                template_name: Template name (provide this or template_id)
                stop_at_cc: Whether to stop at content creation stage
                template_save_mode: Save mode — "draft" or "publish"

            Returns:
                A dictionary containing the API response
            """
            print(f"Editing template category: {template_name or template_id} -> {new_category}", file=sys.stderr)
            try:
                result = edit_template_category(new_category, template_id, template_name, stop_at_cc, template_save_mode)
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        # ---------------------------------------------------------------
        # 2. MESSAGE SENDING TOOLS
        # ---------------------------------------------------------------

        @self.mcp.tool()
        async def send_whatsapp_message(message_payload: Dict[str, Any]) -> Dict[str, Any]:
            """Send a WhatsApp template message (text, media, coupon, carousel, interactive, LTO, order, etc.).

            The payload structure determines the template type. Build the 'message' array
            with recipient_whatsapp, message_type, type_template, and type-specific fields.

            Args:
                message_payload: Full request body. Must contain a 'message' array with objects including:
                    - recipient_whatsapp: Phone number in international format
                    - message_type: e.g. "template", "media_template", "interactive"
                    - type_template: Template name, attributes, language
                    - Additional type-specific fields as needed

            Returns:
                A dictionary containing the API response with message ID
            """
            print(f"Sending WhatsApp message", file=sys.stderr)
            try:
                result = send_template_message(message_payload)
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        # ---------------------------------------------------------------
        # 3. MEDIA TOOLS
        # ---------------------------------------------------------------

        @self.mcp.tool()
        async def get_media_details(media_id: str) -> Dict[str, Any]:
            """Retrieve a WhatsApp media file or its details using its media ID.

            Args:
                media_id: The unique identifier of the media file

            Returns:
                A dictionary containing the media details
            """
            print(f"Fetching media details: {media_id}", file=sys.stderr)
            try:
                result = fetch_media_details(media_id)
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        @self.mcp.tool()
        async def upload_whatsapp_media(file_path: str) -> Dict[str, Any]:
            """Upload a media file (image, video, document) and get a reusable media ID.

            Supported formats: JPEG, PNG, GIF, WebP, MP4, 3GPP, AAC, M4A, AMR,
            OGG OPUS, PDF, DOC, DOCX, PPT, PPTX, XLS, XLSX.

            Args:
                file_path: Local file system path to the media file to upload

            Returns:
                A dictionary containing the uploaded media ID
            """
            print(f"Uploading media: {file_path}", file=sys.stderr)
            try:
                result = upload_media(file_path)
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        @self.mcp.tool()
        async def create_whatsapp_media_handler(file_path: str, media_format: str) -> Dict[str, Any]:
            """Upload a media file and create a handler ID for use in WhatsApp templates.

            Use this to get a handler ID (sample_id) for template HEADER components.

            Args:
                file_path: Local path to the media file (image, video, or document)
                media_format: Media type — "image", "video", or "document"

            Returns:
                A dictionary with sample_id (handler ID) and url
            """
            print(f"Creating media handler: {file_path} ({media_format})", file=sys.stderr)
            try:
                result = create_media_handler(file_path, media_format)
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        # ---------------------------------------------------------------
        # 4. CONSENT MANAGEMENT TOOLS
        # ---------------------------------------------------------------

        @self.mcp.tool()
        async def manage_whatsapp_consent(consent_data: Dict[str, Any]) -> Dict[str, Any]:
            """Register or update user consent (opt-in/opt-out) for WhatsApp messaging.

            Args:
                consent_data: Dictionary with:
                    - type: "optin" or "optout"
                    - recipients: Array of objects with recipient (phone),
                      source (WEB, MOBILE_APP, etc.), user_agent, ip

            Returns:
                A dictionary with processed_count and any failed_recipients
            """
            print(f"Managing consent: {consent_data.get('type', 'unknown')}", file=sys.stderr)
            try:
                result = manage_user_consent(consent_data)
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        @self.mcp.tool()
        async def manage_whatsapp_blocklist(blocklist_data: Dict[str, Any]) -> Dict[str, Any]:
            """Add or remove phone numbers from the blocklist or whitelist.

            Args:
                blocklist_data: Dictionary with:
                    - type: "blocklist" or "whitelist"
                    - recipients: Array of objects with recipient (phone),
                      source, user_agent, ip

            Returns:
                A dictionary with processed_count and any failed_recipients
            """
            print(f"Managing blocklist: {blocklist_data.get('type', 'unknown')}", file=sys.stderr)
            try:
                result = manage_blocklist(blocklist_data)
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        # ---------------------------------------------------------------
        # 5. FLOW TOOLS
        # ---------------------------------------------------------------

        @self.mcp.tool()
        async def get_flow_list(pagination_token: str = None) -> Dict[str, Any]:
            """Retrieve a list of WhatsApp Flows for the WABA.

            Args:
                pagination_token: Optional token for fetching the next page

            Returns:
                A dictionary with flow list and paging cursors
            """
            print("Fetching flow list", file=sys.stderr)
            try:
                result = fetch_flow_list(pagination_token)
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        @self.mcp.tool()
        async def create_whatsapp_flow(flow_data: Dict[str, Any]) -> Dict[str, Any]:
            """Create a new interactive WhatsApp Flow.

            Args:
                flow_data: Dictionary with:
                    - name: Flow name
                    - categories: Array of category strings (e.g. ["OTHER"])
                    - flow_json: JSON string of the flow definition
                    - publish: Optional boolean to publish immediately

            Returns:
                A dictionary with the created flow ID
            """
            print(f"Creating flow: {flow_data.get('name', 'unknown')}", file=sys.stderr)
            try:
                result = create_flow(flow_data)
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        @self.mcp.tool()
        async def publish_whatsapp_flow(flow_id: str) -> Dict[str, Any]:
            """Publish an existing WhatsApp flow, making it live for use.

            Args:
                flow_id: The unique ID of the flow to publish

            Returns:
                A dictionary indicating success or failure
            """
            print(f"Publishing flow: {flow_id}", file=sys.stderr)
            try:
                result = publish_flow(flow_id)
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        @self.mcp.tool()
        async def delete_whatsapp_flow(flow_id: str) -> Dict[str, Any]:
            """Delete an unpublished WhatsApp flow.

            Args:
                flow_id: The unique ID of the flow to delete

            Returns:
                A dictionary indicating success or failure
            """
            print(f"Deleting flow: {flow_id}", file=sys.stderr)
            try:
                result = delete_flow(flow_id)
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        @self.mcp.tool()
        async def deprecate_whatsapp_flow(flow_id: str) -> Dict[str, Any]:
            """Deprecate a published WhatsApp flow, marking it inactive.

            Args:
                flow_id: The unique ID of the flow to deprecate

            Returns:
                A dictionary indicating success or failure
            """
            print(f"Deprecating flow: {flow_id}", file=sys.stderr)
            try:
                result = deprecate_flow(flow_id)
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        @self.mcp.tool()
        async def edit_whatsapp_flow_metadata(flow_id: str, metadata: Dict[str, Any]) -> Dict[str, Any]:
            """Update metadata fields (name, categories) of an existing WhatsApp flow.

            Args:
                flow_id: The unique ID of the flow to edit
                metadata: Dictionary with optional 'name' and 'categories' fields

            Returns:
                A dictionary indicating success or failure
            """
            print(f"Editing flow metadata: {flow_id}", file=sys.stderr)
            try:
                result = edit_flow_metadata(flow_id, metadata)
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        @self.mcp.tool()
        async def get_flow_preview(flow_id: str) -> Dict[str, Any]:
            """Generate a preview URL for a WhatsApp Flow to test before deploying.

            Args:
                flow_id: The unique ID of the flow to preview

            Returns:
                A dictionary with preview_url, expires_at, and flow_id
            """
            print(f"Fetching flow preview: {flow_id}", file=sys.stderr)
            try:
                result = fetch_flow_preview(flow_id)
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        # ---------------------------------------------------------------
        # 6. ANALYTICS TOOLS
        # ---------------------------------------------------------------

        @self.mcp.tool()
        async def get_template_analytics(
            template_id: str,
            date_start: str,
            date_end: str,
            nc_template_id: str = None,
            granularity: str = None,
            limit: int = None,
            use_waba_timezone: bool = None,
            product_type: str = None,
            after: str = None,
            before: str = None,
            metric_types: str = None,
        ) -> Dict[str, Any]:
            """Fetch performance analytics for WhatsApp templates (delivery, read, click, cost, conversion).

            Args:
                template_id: Comma-separated Meta template IDs (up to 10)
                date_start: Start date (YYYY-MM-DD)
                date_end: End date (YYYY-MM-DD)
                nc_template_id: Optional Netcore template ID (single value)
                granularity: Time grouping (e.g. "DAILY")
                limit: Max records per page
                use_waba_timezone: Use WABA timezone for metrics
                product_type: Filter — "CLOUD_API" or "MARKETING_MESSAGES_LITE_API"
                after: Cursor for next page
                before: Cursor for previous page
                metric_types: Comma-separated metric names to return

            Returns:
                A dictionary with analytics data points and paging info
            """
            print(f"Fetching template analytics: {template_id}", file=sys.stderr)
            try:
                result = fetch_template_analytics(
                    template_id, date_start, date_end, nc_template_id,
                    granularity, limit, use_waba_timezone, product_type,
                    after, before, metric_types,
                )
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        # ---------------------------------------------------------------
        # 7. CONVERSATION TOOLS
        # ---------------------------------------------------------------

        @self.mcp.tool()
        async def send_whatsapp_conversation_message(message_data: Dict[str, Any]) -> Dict[str, Any]:
            """Send a WhatsApp conversation message within the 24h customer care window.

            Supports text, image, video, audio, document, sticker, location,
            contacts, and interactive messages (buttons, lists, flows, catalogs).

            Args:
                message_data: Dictionary with:
                    - to: Recipient WhatsApp ID
                    - type: Message type (text, image, video, audio, document, sticker, location, contacts, interactive)
                    - The corresponding type object (e.g. text: {body: "..."})

            Returns:
                A dictionary with the message_id
            """
            print(f"Sending conversation message to: {message_data.get('to', 'unknown')}", file=sys.stderr)
            try:
                result = send_conversation_message(message_data)
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        # ---------------------------------------------------------------
        # 8. CONVERSION TRACKING TOOLS
        # ---------------------------------------------------------------

        @self.mcp.tool()
        async def track_whatsapp_conversions(conversion_data: Dict[str, Any]) -> Dict[str, Any]:
            """Track customer conversion events (CAPI) for Meta ad attribution.

            Supported events: Purchase, Lead, CompleteRegistration, Subscribe,
            StartTrial, AddToCart, InitiateCheckout, ViewContent, etc.

            Args:
                conversion_data: Dictionary with 'data' array of event objects.
                    Each event has: event_name, event_time, action_source,
                    messaging_channel, user_data (mobile_number, ctwa_clid),
                    and optional custom_data.

            Returns:
                A dictionary with events_received count and fbtrace_id
            """
            print(f"Tracking conversions", file=sys.stderr)
            try:
                result = track_conversions(conversion_data)
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        # ---------------------------------------------------------------
        # 9. PAYMENT TOOLS
        # ---------------------------------------------------------------

        @self.mcp.tool()
        async def get_payment_status(payment_configuration: str, reference_id: str) -> Dict[str, Any]:
            """Retrieve the current status of a WhatsApp payment transaction.

            Args:
                payment_configuration: Name of the configured payment setup
                reference_id: Unique ID of the payment transaction

            Returns:
                A dictionary with payment status, amount, and timestamp
            """
            print(f"Fetching payment status: {payment_configuration}/{reference_id}", file=sys.stderr)
            try:
                result = fetch_payment_status(payment_configuration, reference_id)
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        @self.mcp.tool()
        async def process_whatsapp_refund(refund_data: Dict[str, Any]) -> Dict[str, Any]:
            """Initiate a refund for a completed WhatsApp payment transaction.

            Args:
                refund_data: Dictionary with:
                    - reference_id: Payment reference ID
                    - speed: "normal" or "instant"
                    - payment_config_id: Payment configuration name
                    - amount: {currency, value, offset}

            Returns:
                A dictionary with refund_id, amount_refunded, and timestamp
            """
            print(f"Processing refund: {refund_data.get('reference_id', 'unknown')}", file=sys.stderr)
            try:
                result = process_refund(refund_data)
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        @self.mcp.tool()
        async def create_payment_oauth_link(oauth_data: Dict[str, Any]) -> Dict[str, Any]:
            """Generate an OAuth link for payment gateway configuration.

            Args:
                oauth_data: Dictionary with:
                    - configuration_name: Unique name for the payment configuration
                    - redirect_url: HTTPS URL for OAuth callback

            Returns:
                A dictionary with the oauth_url
            """
            print(f"Creating OAuth link: {oauth_data.get('configuration_name', 'unknown')}", file=sys.stderr)
            try:
                result = create_oauth_link(oauth_data)
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        @self.mcp.tool()
        async def create_whatsapp_payment_config(config_data: Dict[str, Any]) -> Dict[str, Any]:
            """Create a new payment gateway configuration for WhatsApp payments.

            Args:
                config_data: Dictionary with:
                    - configuration_name: Unique config name
                    - provider_name: Payment gateway (e.g. "PayU", "RazorPay")
                    - redirect_url: OAuth redirect URL
                    - merchant_category_code: MCC code
                    - purpose_code: Purpose code

            Returns:
                A dictionary with the created configuration details
            """
            print(f"Creating payment config: {config_data.get('configuration_name', 'unknown')}", file=sys.stderr)
            try:
                result = create_payment_configuration(config_data)
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        @self.mcp.tool()
        async def delete_whatsapp_payment_config(configuration_name: str) -> Dict[str, Any]:
            """Delete a payment gateway configuration by name.

            Args:
                configuration_name: The name of the payment configuration to delete

            Returns:
                A dictionary indicating success or failure
            """
            print(f"Deleting payment config: {configuration_name}", file=sys.stderr)
            try:
                result = delete_payment_configuration(configuration_name)
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        # ---------------------------------------------------------------
        # 10. WEBHOOK TOOLS
        # ---------------------------------------------------------------

        @self.mcp.tool()
        async def list_whatsapp_webhooks(webhook_type: str) -> List[Dict[str, Any]]:
            """Retrieve all configured WhatsApp webhooks of a given type.

            Args:
                webhook_type: Webhook type — "incoming" (for chatbot/messages) or "event" (for delivery events)

            Returns:
                A list of webhook configurations with name, URL, status, and type
            """
            print(f"Listing webhooks: {webhook_type}", file=sys.stderr)
            try:
                result = fetch_webhook_list(webhook_type)
                return result or []
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return []

        @self.mcp.tool()
        async def update_whatsapp_webhook(webhook_data: Dict[str, Any]) -> Dict[str, Any]:
            """Create or update a WhatsApp webhook configuration.

            Args:
                webhook_data: Dictionary with:
                    - type: "incoming" or "event"
                    - name: Unique webhook name
                    - url: Destination URL for webhook payloads
                    - source: Optional source/service name
                    - headers: JSON string of custom headers

            Returns:
                A dictionary indicating success or failure
            """
            print(f"Updating webhook: {webhook_data.get('name', 'unknown')}", file=sys.stderr)
            try:
                result = update_webhook(webhook_data)
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        @self.mcp.tool()
        async def manage_whatsapp_webhook_status(manage_data: Dict[str, Any]) -> Dict[str, Any]:
            """Enable or disable a WhatsApp webhook without changing its configuration.

            Args:
                manage_data: Dictionary with:
                    - type: "incoming" or "event"
                    - webhook_name: Name of the webhook
                    - status: "enable" or "disable"

            Returns:
                A dictionary indicating success or failure
            """
            print(f"Managing webhook status: {manage_data.get('webhook_name', 'unknown')}", file=sys.stderr)
            try:
                result = manage_webhook_status(manage_data)
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        # ---------------------------------------------------------------
        # 11. MISCELLANEOUS TOOLS
        # ---------------------------------------------------------------

        @self.mcp.tool()
        async def get_whatsapp_settings() -> Dict[str, Any]:
            """Retrieve the current settings for the WhatsApp Business Account (link tracking, skip opt-in, etc.).

            Returns:
                A dictionary with linktrack and skipoptin settings
            """
            print("Fetching WhatsApp settings", file=sys.stderr)
            try:
                result = fetch_whatsapp_settings()
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        @self.mcp.tool()
        async def get_whatsapp_stats(start_date: str, end_date: str, granularity: str = None) -> Dict[str, Any]:
            """Retrieve WhatsApp message statistics within a date range.

            Args:
                start_date: Start date (YYYY-MM-DD)
                end_date: End date (YYYY-MM-DD)
                granularity: Optional — "day", "week", or "month"

            Returns:
                A dictionary with statistics data including sent, delivered, read, click, failed counts
            """
            print(f"Fetching stats: {start_date} to {end_date}", file=sys.stderr)
            try:
                result = fetch_whatsapp_stats(start_date, end_date, granularity)
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        @self.mcp.tool()
        async def get_whatsapp_messages(start_date: str, end_date: str) -> Dict[str, Any]:
            """Retrieve WhatsApp message details (delivery log) within a date range.

            Args:
                start_date: Start date (YYYY-MM-DD)
                end_date: End date (YYYY-MM-DD)

            Returns:
                A dictionary with message details including status, timestamps, template name
            """
            print(f"Fetching messages: {start_date} to {end_date}", file=sys.stderr)
            try:
                result = fetch_whatsapp_messages(start_date, end_date)
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        @self.mcp.tool()
        async def get_whatsapp_summary_stats(tags: List[str] = None) -> Dict[str, Any]:
            """Retrieve WhatsApp summary statistics filtered by tags.

            Args:
                tags: Optional list of tags to filter statistics

            Returns:
                A dictionary with summary statistics grouped by tag and campaign
            """
            print(f"Fetching summary stats", file=sys.stderr)
            try:
                result = fetch_summary_stats(tags)
                return result or {}
            except Exception as e:
                print(f"Error: {str(e)}", file=sys.stderr)
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
