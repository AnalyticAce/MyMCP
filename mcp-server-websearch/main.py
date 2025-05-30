from openai import OpenAI
from fastmcp import FastMCP
from dotenv import load_dotenv
import os


mcp = FastMCP(
    name="mcp-server-websearch",
    description="A web search server for MCP"
)


load_dotenv(".env")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


@mcp.tool()
def web_search(query: str) -> str:
    """
    Perform a web search using OpenAI's web search tool.

    Args:
        query: The search query to perform.

    Returns:
        A string containing the search results.
    """
    
    client = OpenAI(api_key=OPENAI_API_KEY)
    
    response = client.responses.create(
        model="gpt-3.5-turbo",
        tools=[{"type": "web_search_preview"}],
        input=query
    )
    
    return response.output_text


if __name__ == "__main__":
    mcp.run(transport="stdio")