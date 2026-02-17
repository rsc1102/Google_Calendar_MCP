"""
Quick script to trigger Google OAuth authentication.
This will open a browser window for you to authenticate.
"""
import asyncio
from services import list_events

async def test_auth():
    # This will trigger the OAuth flow if not already authenticated
    result = await list_events(maxResults=1)
    print("Authentication successful!")
    print(f"Result: {result}")

if __name__ == "__main__":
    asyncio.run(test_auth())
