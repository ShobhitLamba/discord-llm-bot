# Heimdall Discord LLM Bot

Heimdall is a Discord bot that answers questions using Anthropic's Claude 3 Haiku 4.5 model. It supports both slash commands and direct mention replies, providing fast, helpful responses in your Discord server.

## Features
- **/ask command**: Use `/ask <question>` to get answers from Claude.
- **Mention-based replies**: Mention the bot (e.g., `@Heimdall what is SpaceX?`) and receive a direct reply.
- **Secure API key handling**: Loads sensitive keys from environment variables or a `.env` file.
- **Docker support**: Easily deploy the bot in a containerized environment.

## Setup

### Prerequisites
- Python 3.11+
- Discord bot token
- Anthropic API key

### Installation
1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd discord-llm-bot
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your credentials:
   ```env
   DISCORD_BOT_TOKEN=your-discord-token
   ANTHROPIC_API_KEY=your-anthropic-key
   ```

### Running Locally
```sh
python heimdall.py
```

### Running with Docker
1. Build the Docker image:
   ```sh
   docker build -t heimdall-bot .
   ```
2. Run the container:
   ```sh
   docker run --env-file .env heimdall-bot
   ```

## Usage
- Use `/ask <question>` in any channel where the bot is present.
- Mention the bot directly with your question for a threaded reply.

## Permissions
Ensure the bot has the following Discord permissions:
- Read Messages
- Send Messages
- Read Message History
- Use Slash Commands

## Environment Variables
- `DISCORD_BOT_TOKEN`: Your Discord bot token
- `ANTHROPIC_API_KEY`: Your Anthropic Claude API key

## License
MIT
