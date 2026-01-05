import discord
from discord import app_commands
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv
from anthropic import Anthropic, AsyncAnthropic

load_dotenv()

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
model = os.getenv("MODEL")
max_tokens = 512
temperature = 0.7

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

async def ask_claude(question: str) -> str:
    api_key = os.getenv("ANTHROPIC_API_KEY")
    client = AsyncAnthropic(api_key=api_key)
    response = await client.messages.create(
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
        system="You are Heimdall, a helpful assistant.",
        messages=[{"role": "user", "content": question}]
    )
    return response.content[0].text

@bot.tree.command(name="ask", description="Ask Claude a question")
@app_commands.describe(
    question="The question you want to ask Claude"
)
async def ask(interaction: discord.Interaction, question: str):
    answer = await ask_claude(question)
    await interaction.response.send_message(answer)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if bot.user in message.mentions:
        question = message.content.replace(f'<@{bot.user.id}>', '').strip()
        if question:
            answer = await ask_claude(question)
            await message.reply(answer, mention_author=False)
    await bot.process_commands(message)

if __name__ == "__main__":
    import sys
    
    # Check for token
    DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
    
    if not DISCORD_BOT_TOKEN:
        print("Error: DISCORD_BOT_TOKEN environment variable not set")
        print("\nTo set your token:")
        print("  export DISCORD_BOT_TOKEN='your-token-here'")
        print("\nOr create a .env file with:")
        print("  DISCORD_BOT_TOKEN=your-token-here")
        sys.exit(1)
    
    bot.run(DISCORD_BOT_TOKEN)

