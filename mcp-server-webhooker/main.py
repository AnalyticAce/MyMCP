from fastmcp import FastMCP
import requests


mcp = FastMCP(
    name="mcp-server-webhooker",
    description="A webhook server for MCP"
)


@mcp.tool()
def send_discord_message(webhook_url: str, message: str) -> str:
    """
    Send a message to a Discord webhook.
    
    Args:
        webhook_url: The Discord webhook URL to send the message to.
        message: The message to send.
    
    Returns:
        Success or failure message
    """
    
    if not webhook_url.startswith("https://discord.com/api/webhooks/"):
        return "Error: Invalid Discord webhook URL."
    
    data = {"content": message}
    try:
        response = requests.post(webhook_url, json=data)
        if response.status_code == 204:
            return "Message sent successfully to Discord."
        else:
            return f"Failed to send Discord message: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error sending Discord message: {str(e)}"


@mcp.tool()
def send_google_chat_message(webhook_url: str, message: str) -> str:
    """
    Send a message to a Google Chat webhook.
    
    Args:
        webhook_url: The Google Chat webhook URL to send the message to.
        message: The message to send.
    
    Returns:
        Success or failure message
    """
    
    if not webhook_url.startswith("https://chat.googleapis.com/v1/spaces/"):
        return "Error: Invalid Google Chat webhook URL."
    
    data = {"text": message}
    try:
        response = requests.post(webhook_url, json=data)
        if response.status_code == 200:
            return "Message sent successfully to Google Chat."
        else:
            return f"Failed to send Google Chat message: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error sending Google Chat message: {str(e)}"


if __name__ == "__main__":
    mcp.run(transport="stdio")