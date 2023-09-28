import requests
import logging
import json

logging.basicConfig(level=logging.INFO)

def get_torrent(search_name):
    url = f"https://torrents-api.ryukme.repl.co/api/all/{search_name}"
    response = requests.get(url)

    try:
        result = json.loads(response.text)
    except json.decoder.JSONDecodeError:
        result = None

    return result

def get_megnate(search_name):
    result_json = get_torrent(search_name)

    if result_json is None:
        return None
    else:
        return result_json
