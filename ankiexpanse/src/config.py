"""Variables shared between modules.

Secret keys should be set as environment variables.
"""

import os

DISCORD_KEY = os.getenv("DISCORD_BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

default_deckname = "anki-helper"
default_modelname = "HSK"
"""
Comment this out if you do not use Docker.
ankiconnect_url = "http://localhost:8765"
"""
ankiconnect_url = "http://host.docker.internal:8765"