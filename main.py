import json
import unicodedata
import psycopg2
from config import config

def parse_json_data():
    with open('stran.json', 'r') as data_file:
        data = data_file.read()

    lyrics = json.loads(data)

    return lyrics

def get_url_friendly_name(artist_name):
    formatted_artist_name = artist_name.lower().replace(' ', '-')
    url_friendly_name =  unicodedata.normalize('NFD', formatted_artist_name).encode('ascii', 'ignore')

    return url_friendly_name.decode('utf-8')

def artist_exists(artist_name):
    artist_exists = False
    connection = None

    try:
        params = config()

        connection = psycopg2.connect(**params)

        cursor = connection.cursor()

        cursor.execute('select exists(select 1 from artist_slugs where name = %s);', (artist_name,))

        artist_exists = cursor.fetchone()[0]

        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

    return artist_exists

# get all lyrics
lyrics = parse_json_data()

for lyric in lyrics:
    url_friendly_artist_name = get_url_friendly_name(lyric['artist_name'])

    artist_does_exist = artist_exists(url_friendly_artist_name)

    if artist_does_exist:
        print(f'artist {url_friendly_artist_name} does exist')
    else:
        print(f'artist {url_friendly_artist_name} does not exist')

    # check to see if artist exists
    # if it does not, add new artist
    # if it does, grab artist id

    # check to see if lyric exists for that artist id 



