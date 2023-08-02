def get_genres(spobj: object, songs: list):
    list = []
    for tracks in songs:
        result = spobj.search(q=tracks, type = 'track', limit=1)
        if result["tracks"]["items"]:
            track_info = spobj.track(result["tracks"]["items"][0]["id"])
            artists = track_info['artists']
            for artist in artists:
                artist_info = spobj.artist(artist["id"])
                genres = artist_info['genres']
                for gen in genres:
                    if gen not in list:
                        list.append(gen)

    return list
            
def format_genres(genres: list):
    genres_list = genres[0].split(',')

    # Remove leading and trailing whitespaces from each genre name
    cleaned_genres = [genre.strip() for genre in genres_list]

    return cleaned_genres

def check_genres(spobj, genres):
    for i in range(len(genres)):
        names = genres[i].lower()
        if "&" in names:
            names = names.replace("&", "-n-")
        if " " in names:
            names = names.replace(" ", "-")
        genres[i] = names
    newList = []
    real_genres = spobj.recommendation_genre_seeds()
    for gen in real_genres['genres']:
        if gen in genres:
            newList.append(gen)
    return newList

def split_into_subsets(input_list, subset_size=5):
    result = []
    for i in range(0, len(input_list), subset_size):
        subset = input_list[i:i + subset_size]
        result.append(subset)
    return result

def recommend(spobj, seed_genre, limit = 50):
    
    recommendations = spobj.recommendations(seed_artists=None, seed_genres=seed_genre, seed_tracks=None, limit=limit, country=None)
    songs = {}
    for i in recommendations["tracks"]:
        artists = [artist['name'] for artist in i["artists"]]
        artists_names = ", ".join(artists)
        songName = i["name"]
        songs[songName] = artists_names
        # print(f"Artist: {artists_names}, Track: {artists_names}")
    return songs

