import json
import unicodedata

def parse_json_data():
    with open('stran.json', 'r') as data_file:
        data = data_file.read()

    lyrics = json.loads(data)

    return lyrics

def get_url_friendly_name(artist_name):
    formatted_artist_name = artist_name.lower().replace(' ', '-')
    url_friendly_name =  unicodedata.normalize('NFD', formatted_artist_name).encode('ascii', 'ignore')

    return url_friendly_name.decode('utf-8')

# get all lyrics
lyrics = parse_json_data()

for lyric in lyrics:
    url_friendly_artist_name = get_url_friendly_name(lyric['artist_name'])

    # check to see if artist exists
    # if it does not, add new artist
    # if it does, grab artist id

    # check to see if lyric exists for that artist id 

    print(url_friendly_artist_name)


