import config
import anki.anki as anki
import ankigpt.ankigpt as ankigpt
import base64
from pathlib import Path

deck_name = config.default_deckname
model_name = config.default_modelname

def generate_and_add_card(query: str, deckname: str):
    note_json: dict = ankigpt.generate_note(query, deckname)
    note_id: int = anki.add_note(note_json)
    print("add note successful")
    sound_filename = Path(__file__).parent / "ankigpt" / note_json["fields"]["Audio"].replace("[sound:", "").replace("]", "")
    # Base64 encode the audio file
    base64_audio = encode_audio_file(sound_filename)
    print(f"Adding audio file {sound_filename.name} to Anki...")
    #store the sound file in anki
    anki.store_media_file(sound_filename.name, base64_audio)
    print(f"Added note with ID {note_id}")

    #delete the sound file
    try:
        sound_filename.unlink()
        print(f"Deleted local file: {sound_filename}")
    except FileNotFoundError:
        print(f"File not found: {sound_filename}")
    except Exception as e:
        print(f"Error deleting file: {e}")
    return note_json, note_id

#encode the audio file as base64
def encode_audio_file(filename: str) -> str:
    print(f"Encoding audio file {filename} as base64...")
    with open(filename, "rb") as file:
        encoded = base64.b64encode(file.read()).decode("utf-8")
    return encoded