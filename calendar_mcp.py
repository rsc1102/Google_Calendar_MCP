from mcp.server.fastmcp import FastMCP
import services

# Initialize FastMCP server
mcp = FastMCP("calendar")


@mcp.tool()
async def list_events(
    summary: str | None = None,
    description: str | None = None,
    location: str | None = None,
    timeMin: str | None = None,
    timeMax: str | None = None,
    maxResults: int = 10,
) -> str:
    """
    Retrieve a list of calendar events based on specified filters.

    This function queries the calendar for events that match the given criteria.
    All filter parameters are optional and can be used in combination to narrow
    down the results.

    Args:
        summary (str, optional): Filter events by their summary (title or subject).
        description (str, optional): Filter events by text found in the event description.
        location (str, optional): Filter events based on their location.
        timeMin (str, optional): ISO 8601 formatted lower time bound (exclusive)
            for filtering events by end time. Must be in local time and have timezone offset. 
        timeMax (str, optional): ISO 8601 formatted upper time bound (exclusive)
            for filtering events by start time. Must be in local time and have timezone offset. 
        maxResults (int, optional): Maximum number of events to return.

    Returns:
        list: A list of event objects that match the provided filters.
    """
    return await services.list_events(
        summary=summary,
        description=description,
        location=location,
        timeMin=timeMin,
        timeMax=timeMax,
        maxResults=maxResults,
    )


if __name__ == "__main__":
    # Run MCP server
    mcp.run(transport="stdio")
