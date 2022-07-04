import psycopg2
from config import config

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

def add_artist(first_name, last_name):
    artist_id = 0
    connection = None
    full_name = f'{first_name} {last_name}'.strip()

    try:
        params = config()

        connection = psycopg2.connect(**params)

        cursor = connection.cursor()

        cursor.execute("insert into artists (first_name, last_name, full_name, is_approved, user_id, created_at, is_deleted, is_imported) values (%s, %s, %s, true, '1871eb29-9752-4c9d-951a-ae17fcb388b2', current_timestamp, false, true) returning id;", (first_name, last_name, full_name))

        record = cursor.fetchone()

        connection.commit()

        artist_id = record[0]

        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

    return artist_id

def add_artist_slug_for_artist(slug, artist_id):
    artist_slug_id = 0
    connection = None

    try:
        params = config()

        connection = psycopg2.connect(**params)

        cursor = connection.cursor()

        cursor.execute('insert into artist_slugs (name, is_primary, created_at, is_deleted, artist_id) values (%s, true, current_timestamp, false, %s) returning id;', (slug, artist_id))

        record = cursor.fetchone()

        connection.commit()

        artist_slug_id = record[0]

        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

    return artist_slug_id


def get_artist_id_by_artist_slug(artist_slug):
    artist_id = 0
    connection = None

    try:
        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()
        cursor.execute('select artist_id from artist_slugs where name = %s;', (artist_slug,))
        artist_id = cursor.fetchone()[0]
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

    return artist_id

def lyric_exists_by_artist_id_and_lyric_slug(artist_id, lyric_slug):
    lyric_exists = False
    connection = None

    try:
        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()
        cursor.execute('select exists(select 1 from artists a left join lyrics l on a.id = l.artist_id left join lyric_slugs ls on l.id = ls.lyric_id where a.id = %s and ls.name = %s);', (artist_id, lyric_slug))
        lyric_exists = cursor.fetchone()[0]
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

    return lyric_exists

def add_lyric_for_artist(title, body, artist_id, youtube_link):
    lyric_id = 0
    connection = None

    try:
        params = config()

        connection = psycopg2.connect(**params)

        cursor = connection.cursor()

        cursor.execute("insert into lyrics (title, body, user_id, created_at, is_deleted, is_approved, artist_id, is_imported, youtube_link) values (%s, %s, '1871eb29-9752-4c9d-951a-ae17fcb388b2', current_timestamp, false, true, %s, true, %s) returning id;", (title, body, artist_id, youtube_link))

        record = cursor.fetchone()

        connection.commit()

        lyric_id = record[0]

        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

    return lyric_id

def add_lyric_slug_for_lyric(slug, lyric_id):
    lyric_slug_id = 0
    connection = None

    try:
        params = config()

        connection = psycopg2.connect(**params)

        cursor = connection.cursor()

        cursor.execute('insert into lyric_slugs (name, is_primary, created_at, is_deleted, lyric_id) values (%s, true, current_timestamp, false, %s) returning id;', (slug, lyric_id))

        record = cursor.fetchone()

        connection.commit()

        lyric_slug_id = record[0]

        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

    return lyric_slug_id
