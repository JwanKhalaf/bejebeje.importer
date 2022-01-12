import json
from db import *
from helpers import *

def parse_json_data():
    with open('stran.json', 'r') as data_file:
        data = data_file.read()

    lyrics = json.loads(data)

    return lyrics

# get all lyrics
lyrics = parse_json_data()

for lyric in lyrics:
    artist_full_name = lyric['artist_name']
    artist_slug = get_artist_slug(artist_full_name) 
    lyric_title = lyric['lyric_title']
    lyric_slug = get_lyric_slug(lyric_title)
    lyric_body = lyric['lyric_body']
    lyric_link = lyric['youtube_link']

    artist_does_exist = artist_exists(artist_slug)

    artist_id = 0

    if artist_does_exist:
        artist_id = get_artist_id_by_artist_slug(artist_slug)
    else:
        head, sep, tail = artist_full_name.partition(' ')
        first_name = head.lower()
        last_name = tail.lower()

        artist_id = add_artist(first_name, last_name)

        if artist_id == 0:
            raise ValueError(f'artist id for {artist_full_name} is 0')

        artist_slug_id = add_artist_slug_for_artist(artist_slug, artist_id)

    if artist_id != 0:
        lyric_does_exist = lyric_exists_by_artist_id_and_lyric_slug(artist_id, lyric_slug)

        if lyric_does_exist:
            pass
        else:
            lyric_id = add_lyric_for_artist(lyric_title, lyric_body, artist_id, lyric_link)

            if lyric_id == 0:
                raise ValueError(f'lyric id for the lyric {lyric_title} by {artist_full_name} is 0')

            lyric_slug_id = add_lyric_slug_for_lyric(lyric_slug, lyric_id)

