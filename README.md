# Google Calendar MCP Server ![Anthropic](https://img.shields.io/badge/Anthropic-ffffff?logo=anthropic&logoColor=black) ![Claude](https://img.shields.io/badge/Claude-ffffff?logo=claude&logoColor=orange)

This repository provides a Model Context Protocol (MCP) server that integrates with the Google Calendar API. It allows users to list, create, delete, and update calendar events. The server is designed to work with Anthropic's Claude Desktop as an MCP client.

## 🚀 Features
- Interact with Google Calendar: list, add, delete, and update events
- Seamless integration with Claude Desktop via MCP

---

## 🧰 Prerequisites
- A Google Account
- [Anthropic Claude Desktop](https://claude.ai/download)

---

## 📦 Installation

1. **Install UV Package Manager:**
   Follow the instructions on the [official UV installation guide](https://docs.astral.sh/uv/getting-started/installation/#installation-methods).

2. **Clone the Repository and Set Up Environment:**
   ```bash
   git clone https://github.com/rsc1102/Google_Calendar_MCP.git
   cd Google_Calendar_MCP
   uv sync
   ```

3. **Create Google Cloud Credentials:**
   - Visit [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project or select an existing one.
   - Enable the **Google Calendar API**.
   - Navigate to **APIs & Services > Credentials**.
   - Click **Create Credentials > OAuth Client ID**:
     - Choose **Desktop app** as the application type.
     - Download the generated `credentials.json` file.
     - Place `credentials.json` inside the `Google_Calendar_MCP` directory.

---

## 🔌 Integration with Claude Desktop

1. **Locate Configuration File:**
   Open the `claude_desktop_config.json` file on your system:

   **Linux/macOS:**
   ```bash
   code ~/Library/Application\ Support/Claude/claude_desktop_config.json
   ```

   **Windows (PowerShell):**
   ```bash
   code $env:AppData\Claude\claude_desktop_config.json
   ```

2. **Add MCP Server Configuration:**
   Add the following to the `mcpServers` section:
   ```json
   {
       "mcpServers": {
           "calendar": {
               "command": "uv",
               "args": [
                   "--directory",
                   "/ABSOLUTE/PATH/TO/PARENT/FOLDER/Google_Calendar_MCP",
                   "run",
                   "calendar_mcp.py"
               ]
           }
       }
   }
   ```

3. **Restart Claude Desktop.**

4. **Create a New Project in Claude Desktop.**

5. **Set Timezone:**
   In the project's knowledge section, define your local timezone using the IANA Time Zone format (e.g., `timeZone="America/New_York"`).

6. **Start Chatting:**
   Begin interacting with Claude to manage your Google Calendar events.   
   **Note:** When using the server for the first time, Google will prompt you to authenticate and grant permission to access your calendar.

---

## 📬 Support
For issues or questions, please open an issue in this repository.
