from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("{{ cookiecutter.service_name }}")


@mcp.prompt("example-prompt")
def example_prompt(name: str) -> str:
    """Example prompt"""
    return f"Hello, {name}!"


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
