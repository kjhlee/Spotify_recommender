def get_Top(spobj: object):
    results = spobj.current_user_top_tracks(limit = 50, time_range = "short_term")
    songNames = []
    for i in results["items"]:
        songNames.append(i["name"])
    return songNames

def get_track_uri(spobj: object, list_of_songs: dict):
    track_uri = []
    for songs in list_of_songs:
        result = spobj.search(q=songs, type = "track", limit = 1)
        if result["tracks"]["items"]:
            song_uri = result["tracks"]["items"][0]["uri"]
            song_uri = song_uri.split(":")[-1]
            track_uri.append(song_uri)

    return track_uri


def get_recent_fifty(spobj: object):
    recent = spobj.current_user_recently_played(limit = 50)
    songNames = []
    for i in recent["items"]:
        songNames.append(i["track"]["name"])
    return songNames
