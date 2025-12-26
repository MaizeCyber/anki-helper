import os
import json
from openai import OpenAI
from pathlib import Path
from gtts import gTTS
import hashlib
import random
import string


JSON_INSTRUCTION = "You are a system that only outputs JSON."

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def generate(system_prompt: str, user_prompt: str) -> str:
    completion = client.chat.completions.create(
        #modified model to gpt-3.5-turbo-0125
        model="gpt-3.5-turbo-0125",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return completion.choices[0].message.content

#generates a sound by calling the OpenAI API
def generate_sound(text: str, deckname: str) -> str:
    unique_filename = add_hash_suffix_to_file_stem("speech.mp3")
    print(f"Generating sound file: {unique_filename}")
    speech_file_path = Path(__file__).parent / unique_filename
    print(f"speech_file_path: {speech_file_path}")
    if deckname == "chinese":
        language = "zh-CN"
    elif deckname == "spanish":
        language = "es"
    elif deckname == "japanese":
        language = "ja"
    response = gTTS(text=text, lang=language)
    response.save(speech_file_path)
    return unique_filename

def generate_json(
        system_prompt: str,
        user_prompt: str,
        examples: str = "") -> dict:
    json_prompt = JSON_INSTRUCTION + system_prompt + examples
    generated_json: str = generate(json_prompt, user_prompt)
    return json.loads(generated_json)

#randon file name generator for sound file
def add_hash_suffix_to_file_stem(fname: str) -> str:
    # Generate a random 20-byte hash
    hash_value = hashlib.sha1(''.join(random.choices(string.ascii_letters + string.digits, k=20)).encode()).hexdigest()
    max_len = 255 - len(hash_value) - 1  # Adjust for filename max length

    # Separate filename stem and extension
    stem, ext = Path(fname).stem[:max_len], Path(fname).suffix
    return f"{stem}-{hash_value}{ext}"