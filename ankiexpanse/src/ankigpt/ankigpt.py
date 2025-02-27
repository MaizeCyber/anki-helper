"""Generates JSON usable with AnkiConnect from natural language queries.

New version for other languages. Tested on Chinese, spanish, and Japanese

Example Usage:
    note_json: dict = ankigpt.generate_note("苹果")

"""

from . import llm
from . import prompts

def generate_note(query: str, deckname: str) -> dict:
    print("Generating note...")
    if deckname == "chinese":
        promptInstruction = prompts.EXAMPLES_HSK
    elif deckname == "spanish":
        promptInstruction = prompts.EXAMPLES_ROMANTIC
    elif deckname == "japanese":
        promptInstruction = prompts.EXAMPLES_JAPONIC

    system_prompt = "".join(
        [
            prompts.ANKIHELPER_INSTRUCTION,
            prompts.DECKNAME_INSTRUCTION
        ]
    )
    print("system_prompt: ", system_prompt)
    print("query: ", query)
    print("promptInstruction: ", promptInstruction)
    note_json = llm.generate_json(
        system_prompt, 
        query,
        promptInstruction
    )

    with_speech_note_json = add_audio_to_note_json(note_json, llm.generate_sound(query, deckname))
    print("with_speech_note_json: ", with_speech_note_json)
    return with_speech_note_json

# function to add string of mp3 filename to "Audio" field of note_json in the format     "SentenceAudio": "[sound:audiofile.mp3]"
def add_audio_to_note_json(note_json: dict, audio_filename: str) -> dict:
    note_json["fields"]["Audio"] = f"[sound:{audio_filename}]"
    return note_json