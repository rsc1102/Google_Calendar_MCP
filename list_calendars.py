"""List all available Google Calendars and their IDs."""
import asyncio
from services import calender_service

async def list_calendars():
    service = calender_service()
    result = service.calendarList().list().execute()
    for cal in result.get("items", []):
        print(f"  Name: {cal['summary']}")
        print(f"  ID:   {cal['id']}")
        print(f"  Primary: {cal.get('primary', False)}")
        print()

if __name__ == "__main__":
    asyncio.run(list_calendars())
