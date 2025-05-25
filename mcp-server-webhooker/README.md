# MCP Server Webhooker

A Model Context Protocol (MCP) server that enables sending messages to various webhook services including Discord and Google Chat. This server provides tools that can be used by MCP-compatible clients like Claude Desktop or VS Code with MCP extensions.

## Features

- **Discord Webhook Integration**: Send messages to Discord channels via webhooks
- **Google Chat Webhook Integration**: Send messages to Google Chat spaces via webhooks
- **FastMCP Framework**: Built using the FastMCP framework for easy development and deployment
- **Error Handling**: Robust error handling with descriptive error messages

## Available Tools

### `send_discord_message`
Send a message to a Discord channel using a webhook URL.

**Parameters:**
- `webhook_url` (string): The Discord webhook URL (must start with `https://discord.com/api/webhooks/`)
- `message` (string): The message content to send

**Returns:**
- Success or failure message

### `send_google_chat_message`
Send a message to a Google Chat space using a webhook URL.

**Parameters:**
- `webhook_url` (string): The Google Chat webhook URL (must start with `https://chat.googleapis.com/v1/spaces/`)
- `message` (string): The message content to send

**Returns:**
- Success or failure message

## Installation

### Prerequisites

- Python 3.8 or higher
- uv (recommended) or pip for package management

### Install Dependencies

Using uv (recommended):
```bash
uv sync
```

Using pip:
```bash
uv add fastmcp requests
```

## Usage

### Running the Server

```bash
uv run main.py
```

The server runs on stdio transport, making it compatible with MCP clients.

## VS Code Integration

To use this MCP server with VS Code, you'll need to install an MCP extension and configure it to use this server.

### Step 1: Install MCP Extension

1. Open VS Code
2. Go to Extensions (Ctrl/Cmd + Shift + X)
3. Search for "MCP" or "Model Context Protocol"
4. Install a compatible MCP extension (such as "MCP Client" or similar)

### Step 2: Configure the MCP Server

1. Open VS Code settings (Ctrl/Cmd + ,)
2. Search for "MCP" in settings
3. Find the MCP server configuration section
4. Add a new server configuration:

```json
{
  "name": "webhooker",
  "command": "/path/to/your/mcp-server-webhooker/.venv/bin/python",
  "args": ["/path/to/your/mcp-server-webhooker/main.py"],
  "env": {}
}
```

Replace `/path/to/your/mcp-server-webhooker/main.py` with the actual path to your `main.py` file.

### Step 3: Restart VS Code

After adding the configuration, restart VS Code to load the MCP server.

### Step 4: Using the Tools

Once configured, you can use the webhook tools in VS Code:

1. Open the MCP panel or command palette
2. Look for the available tools: `send_discord_message` and `send_google_chat_message`
3. Provide the required parameters (webhook URL and message)
4. Execute the tool to send messages

## Getting Webhook URLs

### Discord Webhook

1. Go to your Discord server
2. Right-click on the channel you want to send messages to
3. Select "Edit Channel"
4. Go to "Integrations" tab
5. Click "Create Webhook"
6. Copy the webhook URL

### Google Chat Webhook

1. Open Google Chat in your browser
2. Go to the space you want to send messages to
3. Click on the space name at the top
4. Select "Manage webhooks"
5. Click "Add webhook"
6. Copy the webhook URL

## Example Usage

Once the server is running and connected to your MCP client:

```python
# Send a Discord message
send_discord_message(
    webhook_url="https://discord.com/api/webhooks/your-webhook-id/your-webhook-token",
    message="Hello from MCP!"
)

# Send a Google Chat message
send_google_chat_message(
    webhook_url="https://chat.googleapis.com/v1/spaces/your-space-id/messages?key=your-key&token=your-token",
    message="Hello from MCP!"
)
```

## Error Handling

The server includes comprehensive error handling:

- **Invalid URLs**: Validates webhook URL formats
- **Network Errors**: Handles connection issues and timeouts
- **API Errors**: Reports HTTP status codes and error messages
- **General Exceptions**: Catches and reports unexpected errors

## Development

### Project Structure

```
mcp-server-webhooker/
├── main.py              # Main server implementation
├── pyproject.toml       # Project configuration
├── README.md           # This file
└── uv.lock            # Dependency lock file
```

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test your changes
5. Submit a pull request

## License

This project is open source. Please check the license file for details.

## Support

For issues and questions:
1. Check the error messages returned by the tools
2. Verify webhook URLs are correct and accessible
3. Ensure the MCP server is properly configured in your client
4. Check the server logs for additional debugging information