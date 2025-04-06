import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from datetime import datetime


class CalenderService:
    def __init__(self):
        self.__calender_service = None
        self.__scope = ["https://www.googleapis.com/auth/calendar"]

    def __call__(self):
        """
        Returns a Calendar API service object.
        """
        if self.__calender_service is None:
            try:
                creds = None
                # Check if token.json file exists with saved credentials
                if os.path.exists("token.json"):
                    creds = Credentials.from_authorized_user_file(
                        "token.json", self.__scope
                    )

                # If credentials don't exist or are invalid, get new ones
                if not creds or not creds.valid:
                    if creds and creds.expired and creds.refresh_token:
                        creds.refresh(Request())
                    else:
                        # flow instance using client secrets file from Google Cloud Console
                        flow = InstalledAppFlow.from_client_secrets_file(
                            "credentials.json", self.__scope
                        )
                        # Run the authorization flow in local server mode
                        creds = flow.run_local_server(port=0)

                    # Save the credentials for the next run
                    with open("token.json", "w") as token:
                        token.write(creds.to_json())

                # Build and return the service object
                self.__calender_service = build("calendar", "v3", credentials=creds)
            except Exception:
                print("Calendar service could not be initialized")

        return self.__calender_service


# singleton
calender_service = CalenderService()


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
    service = calender_service()
    if service is None:
        return "Unable to communicate with the Google Calendar Service."

    # datetime validation
    try:
        if timeMin is None:
            timeMin = datetime.now().astimezone().isoformat()
        timeMin = datetime.fromisoformat(timeMin).astimezone().isoformat()
    except Exception:
        return "timeMin in incorrect format. It should be in ISO format"

    try:
        timeMax = datetime.fromisoformat(timeMax).astimezone().isoformat() if timeMax is not None else None
    except Exception:
        return "timeMax in incorrect format. It should be in ISO format"


    try:
        maxResults = int(maxResults)
    except Exception:
        maxResults = 10

    search_parameters = [x for x in [summary, description, location] if x is not None]
    search_query = " ".join(search_parameters)
    
    print(timeMin)

    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=timeMin,
            timeMax=timeMax,
            maxResults=maxResults,
            singleEvents=True,
            orderBy="startTime",
            q=search_query,
        )
        .execute()
    )

    events = events_result.get("items", [])

    if not events:
        return "No upcoming events found."

    events_info = []
    for i, event in enumerate(events):
        start = event["start"].get("dateTime", event["start"].get("date"))
        if start:
            start = (
                datetime.fromisoformat(start).astimezone().strftime("%Y-%m-%d %H:%M:%S")
            )
        end = event["end"].get("dateTime", event["end"].get("date"))
        if end:
            end = datetime.fromisoformat(end).astimezone().strftime("%Y-%m-%d %H:%M:%S")
        summary = event.get("summary", "N/A")
        description = event.get("description", "N/A")
        location = event.get("location", "N/A")

        event_info = f"""
index: {i + 1}
start: {start}
end: {end}
summary: {summary}
description: {description}
location: {location}
"""

        events_info.append(event_info)

    return "\n--\n".join(events_info)
