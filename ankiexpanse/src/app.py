"""Discord app for AnkiHelper

1. LLM Interaction
    Prompt + Parsing response into JSON 
2. Sending JSON object to Anki Connect
    Figure out how to do a shared deck

Usage (with `anki-helper` as active directory):
    python3 src/app.py
"""

import json
import discord
from discord.ext import commands
import config, create

# Initialize intents
intents = discord.Intents.default()
intents.message_content = True #v2
intents.messages = True  # Enable message intents

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command(name="add")
async def add(ctx, arg1, arg2):
    #check number of arguments
    if len(arg1) == 0 or len(arg2) == 0:
        await ctx.send("Please provide a query and a deck name, separated by a space. Use quotes for phrases.")
        return
    query = arg1
    deckname = arg2
    # Remove the command prefix and the command name from the message to get the raw arguments
    try: 
        await ctx.send(f"Creating an example with query `{query}` in deck '{deckname}'. . .")
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
        await ctx.send(f"Uh oh, something went wrong: `"+str(e)+"`")
        print(f'Error: {e}')

bot.run(config.DISCORD_KEY)