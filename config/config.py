import json
from pathlib import Path
CONFIG_PATH = Path(__file__).parent / "settings.json"
with open(CONFIG_PATH, "r") as file:
    settings =json.load(file)

BASE_URL = settings["base_url"]
BROWSER = settings["browser"]
IMPLICIT_WAIT = settings["implicit_wait"]
EXPLICIT_WAIT =settings["explicit_wait"]

