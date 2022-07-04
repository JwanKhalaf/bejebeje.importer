import unicodedata

def get_artist_slug(name):
    formatted_artist_name = name.lower().replace(' ', '-').replace('ı','i')
    artist_slug =  unicodedata.normalize('NFD', formatted_artist_name).encode('ascii', 'ignore')

    return artist_slug.decode('utf-8')

def get_lyric_slug(title):
    formatted_title = title.lower().replace(' ', '-').replace('ı','i')
    lyric_slug =  unicodedata.normalize('NFD', formatted_title).encode('ascii', 'ignore')

    return lyric_slug.decode('utf-8')
