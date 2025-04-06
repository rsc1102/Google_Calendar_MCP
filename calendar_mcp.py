from mcp.server.fastmcp import FastMCP
import services

# Initialize FastMCP server
mcp = FastMCP("calendar")


@mcp.tool()
async def list_events(
    timeMin: str | None = None, timeMax: str | None = None, maxResults: int = 10
) -> str:
    """Get list of events on the calendar.

    Args:
        timeMin: Lower bound (exclusive) for an event's end time to filter by. Must be in ISO format.
        timeMax: Upper bound (exclusive) for an event's start time to filter by. Must be in ISO format.
        maxResults: Maximum number of events to filter.
    """
    return await services.list_events(
        timeMin=timeMin, timeMax=timeMax, maxResults=maxResults
    )
    
if __name__ == "__main__":
    # Run MCP server
    mcp.run(transport='stdio')
