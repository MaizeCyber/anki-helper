import json
import discord
from discord.ext import commands
import config, create
from pathlib import Path
import asyncio

# Initialize intents
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True  # Enable message intents

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command(name="add")
async def add(ctx, arg1, arg2):
    # Check number of arguments
    if len(arg1) == 0 or len(arg2) == 0:
        await ctx.send("Please provide a query and a deck name, separated by a space. Use quotes for phrases.")
        return
    query = arg1
    deckname = arg2
    try:
        await ctx.send(f"Creating an example with query `{query}` in deck '{deckname}'...")
        note_json, note_id = create.generate_and_add_card(query, deckname)
        confirmation = "".join(
            [
                "Done! Added **",
                note_json["fields"]["Key"],
                "** to deck **",
                note_json["deckName"],
                "**."
            ]
        )
        note_json = json.dumps(note_json, indent=2, ensure_ascii=False)
        message = f"{confirmation}\n```json\n{note_json}```"
        await ctx.send(message)

    except Exception as e:
        await ctx.send(f"Uh oh, something went wrong: `{str(e)}`")
        print(f"Error: {e}")

@bot.command(name="add_from_file")
async def add_from_file(ctx, deck_name: str, file_path: str):
    """Process a text file and create cards for each word."""
    try:
        file = Path(file_path)
        if not file.exists():
            await ctx.send(f"File `{file_path}` not found.")
            return

        await ctx.send(f"Processing file `{file_path}` for deck `{deck_name}`...")

        with file.open("r", encoding="utf-8") as f:
            words = [line.strip() for line in f if line.strip()]

        for word in words:
            try:
                await ctx.send(f"Creating a card for `{word}`...")
                note_json, note_id = create.generate_and_add_card(word, deck_name)
                confirmation = f"Added **{note_json['fields']['Key']}** to deck **{note_json['deckName']}**."
                await ctx.send(confirmation)
                # Introduce a delay to avoid overwhelming APIs
                await asyncio.sleep(2)
            except Exception as e:
                await ctx.send(f"Failed to add `{word}`: `{str(e)}`")
                print(f"Error adding `{word}`: {e}")

        await ctx.send("File processing completed.")
    except Exception as e:
        await ctx.send(f"An error occurred while processing the file: `{str(e)}`")
        print(f"Error processing file: {e}")

bot.run(config.DISCORD_KEY)
