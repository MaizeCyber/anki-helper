"""Wrapper for requests to ankiconnect.

Simplifies requests to AnkiConnect with the `invoke()` function. Clarifies error messages with error raising. Suggested by AnkiConnect dev: https://foosoft.net/projects/anki-connect/.

Examples:
    response: dict = ankiconnect.invoke("deckNames")

    params = {"deck": "Biology"}
    response = ankiconnect.invoke(action="createDeck",**params)
"""

import json
import urllib.request
import urllib.error

""" This is edited to work with a Docker container rather than local host. If you are not running this with docker. uncomment the DEFAULT_URL line and replace the docker url.
DEFAULT_URL = "http://localhost:8765"
"""
DEFAULT_URL = "http://host.docker.internal:8765"
url = DEFAULT_URL

def reset_url() -> None:
    global url
    url = DEFAULT_URL

def set_url(new_url: str) -> None:
    global url
    url = new_url

def format_request(action: str, **params) -> dict:
    return {"action": action, "params": params, "version": 6}

def invoke(action: str, **params) -> dict:
    """Makes a request to AnkiConnect to perform an action using given params.

    Args:
        action: desired action from AnkiConnect. Supported actions are named identical to AnkiConnect actions.
        **params: contextual info relevant to the action

    Returns:
        A dict with "result" and "error" keys.

    Raises:
        - Exception: generic error 😭
    """
    # format and send request
    request_dict: dict = format_request(action, **params)
    request_json: str = json.dumps(request_dict).encode("utf-8")

    #additional debugging
    try:
        request = urllib.request.urlopen(urllib.request.Request(url, request_json))

    except urllib.error.URLError as e:
        raise Exception(f"Failed to reach the server: {e.reason}")
    except urllib.error.HTTPError as e:
        raise Exception(f"Server couldn't fulfill the request. Error code: {e.code}")

    try:
        response: dict = json.load(request)
    except json.JSONDecodeError:
        raise Exception("Failed to decode JSON response")

    # Raise errors if any
    if len(response) != 2:
        raise Exception("Response has an unexpected number of fields")
    if "error" not in response:
        raise Exception("Response is missing required error field")
    if "result" not in response:
        raise Exception("Response is missing required result field")
    if response["error"] is not None:
        raise Exception(response["error"])

    return response