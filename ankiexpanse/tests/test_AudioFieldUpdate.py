import requests
import json
import time
from pathlib import Path
from gtts import gTTS
import hashlib
import random
import string
import base64

# AnkiConnect URL
ANKI_CONNECT_URL = "http://localhost:8765/"

# Utility function to add hash suffix to file stem
def add_hash_suffix_to_file_stem(fname: str) -> str:
    hash_value = hashlib.sha1(
        ''.join(random.choices(string.ascii_letters + string.digits, k=20)).encode()
    ).hexdigest()
    max_len = 255 - len(hash_value) - 1  # Adjust for filename max length
    stem, ext = Path(fname).stem[:max_len], Path(fname).suffix
    return f"{stem}-{hash_value}{ext}"

# Generate sound file using gTTS
def generate_sound(text: str, deckname: str) -> str:
    unique_filename = add_hash_suffix_to_file_stem("speech.mp3")
    speech_file_path = Path(__file__).parent / unique_filename
    print(f"Saving TTS audio to: {speech_file_path}")
    language = "zh-CN"  # Assuming the deck is "Chinese"
    response = gTTS(text=text, lang=language)
    response.save(speech_file_path)
    return str(speech_file_path)

# AnkiConnect request
def anki_request(action: str, params: dict = None) -> dict:
    if params is None:
        params = {}
    try:
        response = requests.post(
            ANKI_CONNECT_URL,
            json={"action": action, "version": 6, "params": params}
        ).json()
    except Exception as e:
        print(f"Request to AnkiConnect failed: {e}")
        return {"error": str(e)}
    if response.get('error'):
        print(f"AnkiConnect Error [{action}]: {response['error']}")
    return response

# Find all notes in the "Chinese" deck
def find_notes(deck_name: str):
    params = {"query": f"deck:{deck_name}"}
    response = anki_request("findNotes", params)
    return response.get("result", [])

# Get information for notes
def get_note_info(note_ids):
    params = {"notes": note_ids}
    response = anki_request("notesInfo", params)
    return response.get("result", [])

# Store media file in Anki
def store_media(file_path: str):
    with open(file_path, "rb") as file:
        media_data = base64.b64encode(file.read()).decode("utf-8")
    filename = Path(file_path).name
    print(f"Adding media file '{filename}' to Anki...")
    response = anki_request("storeMediaFile", {"filename": filename, "data": media_data})
    if response.get("error"):
        print(f"Failed to upload media file '{filename}': {response['error']}")
        return False
    elif response.get("result") == filename:
        return True
    else:
        print(f"Unexpected response when uploading media file '{filename}': {response}")
        return False

# Update a note in Anki
def update_note(note_id, audio_file):
    params = {
        "note": {
            "id": note_id,
            "fields": {
                "Audio": f"[sound:{audio_file}]"
            }
        }
    }
    response = anki_request("updateNoteFields", params)
    if response.get('error'):
        print(f"Failed to update note {note_id}: {response['error']}")
        return False
    else:
        return True

# Main process
def process_deck(deck_name: str):
    note_ids = find_notes(deck_name)
    if not note_ids:
        print("No notes found.")
        return

    notes = get_note_info(note_ids)
    for note in notes:
        note_id = note['noteId']
        fields = note['fields']
        audio_field = fields.get("Audio", {}).get("value", "")

        # Skip if Audio field already has content
        if audio_field.strip():
            print(f"Skipping note {note_id}, Audio field already populated.")
            continue

        # Extract Key field for TTS
        key_text = fields.get("Key", {}).get("value", "")
        if not key_text.strip():
            print(f"Skipping note {note_id}, Key field is empty.")
            continue

        # Generate TTS audio
        print(f"Processing note {note_id}, generating audio for '{key_text}'...")
        sound_file_path = generate_sound(key_text, deck_name)

        # Upload audio to Anki
        if store_media(sound_file_path):
            audio_file_name = Path(sound_file_path).name
            print(f"Audio file '{audio_file_name}' uploaded successfully.")

            # Update note with audio file name
            if update_note(note_id, audio_file_name):
                print(f"Note {note_id} updated with audio file '[sound:{audio_file_name}]'.")
            else:
                print(f"Failed to update note {note_id}.")
        else:
            print(f"Failed to upload audio file for note {note_id}.")

        # Wait before processing next note to avoid overwhelming TTS API
        time.sleep(2)

if __name__ == "__main__":
    process_deck("Chinese")
