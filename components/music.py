import json
from datetime import datetime
from pathlib import Path


def weekly_song():

    song_file = Path("assets/songs.json")

    if not song_file.exists():

        return {
            "title":"No Song",
            "artist":"Unknown",
            "link":""
        }

    with open(song_file, encoding="utf-8") as f:

        songs = json.load(f)

    week = datetime.today().isocalendar().week

    return songs[week % len(songs)]