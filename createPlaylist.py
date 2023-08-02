

def create_playlist(spobj: object, name: str, description: str, public=True):
    sp = spobj
    user_id = sp.current_user()["id"]
    playlist = sp.user_playlist_create(user=user_id, name=name, public=public, description=description)
    return playlist


def get_playlist_id(spobj: object, playlist_name: str):
    playlists = spobj.current_user_playlists()
    for name in playlists["items"]:
        if name["name"] == playlist_name:
            return name["id"]
    return None

def add_to_playlist(spobj: object, playlist_id: str, list_of_uri: list):
    if spobj.playlist_add_items(playlist_id, list_of_uri):
        return "Success"
    return None

