songplay_table_drop = "DROP TABLE sparkify.songplays"
user_table_drop = "DROP TABLE sparkify.users"
song_table_drop = "DROP TABLE sparkify.songs"
artist_table_drop = "DROP TABLE sparkify.artists"
time_table_drop = "DROP TABLE sparkify.time"

songplay_table_create = """CREATE TABLE songplays(
        songplay_id SERIAL,
        start_time TIMESTAMP REFERENCES time(start_time),
        user_id VARCHAR(50) REFERENCES users(user_id),
        level VARCHAR(50),
        song_id VARCHAR(100) REFERENCES songs(song_id),
        artist_id VARCHAR(100) REFERENCES artists(artist_id),
        session_id BIGINT,
        location VARCHAR(255),
        user_agent TEXT,
        PRIMARY KEY(song_id)
    )
    """

user_table_create = """CREATE TABLE users(
        user_id VARCHAR,
        firstName VARCHAR(255),
        lastName VARCHAR(255),
        gender VARCHAR(1),
        level VARCHAR(50),
        PRIMARY KEY(user_id)
    )
    """

songs_table_create = """CREATE TABLE songs(
        song_id VARCHAR(100),
        title VARCHAR(255),
        artist_id VARCHAR(100),
        year INTEGER,
        duration DOUBLE PRECISION,
        PRIMARY KEY(song_id)
    )
    """

artist_table_create = """CREATE TABLE artists(
        artist_id VARCHAR(100),
        name VARCHAR(255),
        location VARCHAR(255),
        latitude DOUBLE PRECISION,
        longitude DOUBLE PRECISION,
        PRIMARY KEY (artist_id)
    )
    """

time_table_create = """CREATE TABLE time(
        start_time TIMESTAMP,
        hour INTEGER,
        day INTEGER,
        week INTEGER,
        month INTEGER,
        year INTEGER,
        weekday INTEGER,
        PRIMARY KEY (start_time)
    )
    """

songplay_table_insert = """INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
 VALUES (?, ?, ?, ?, ?, ?, ?, ?) """

user_table_insert = """INSERT INTO users (user_id, firstName, lastName, gender, level) VALUES (?, ?, ?, ?, ?) 
ON CONFLICT (user_id) DO UPDATE SET firstName=users.firstName, lastName=users.lastName, gender=users.gender, level=users.level """

song_table_insert = """INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (?, ?, ?, ?, ?)
ON CONFLICT (song_id) DO UPDATE SET title=songs.title, artist_id=songs.artist_id,
year=songs.year, duration=songs.duration """

artist_table_insert = """INSERT INTO artists (artist_id, name, location, latitude, longitude) VALUES (?, ?, ?, ?, ?)
ON CONFLICT (artist_id) DO UPDATE SET name=artists.name, location=artists.location, latitude=artists.latitude, 
longitude=artists.longitude """

time_table_insert = """INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (?, ?, ?, ?, ?, ?, ?)
ON CONFLICT (start_time) DO UPDATE SET hour=time.hour, day=time.day, week=time.week, month=time.month, 
year=time.year, weekday=time.weekday """

# FIND SONGS BY SONG_ID AND ARTIST_ID
song_select_by_song_id_artist_id = """SELECT s.song_id, a.artist_id FROM songs s, artists a
WHERE s.artist_id = a.artist_id  
    AND s.title = ?
    AND a.name = ?
    AND s.duration = ?
"""

# FIND SONG BY ID
song_select = "SELECT COUNT(*) FROM songs s WHERE s.song_id = ?"

# FIND ARTIST BY ID
artist_select = """SELECT COUNT(*) FROM artists a
WHERE a.artist_id = ?
"""

# FIND USER BY ID
user_select = """SELECT COUNT(*) FROM users u
WHERE u.user_id = ?
"""

# FIND TIME BY ID
time_select = "SELECT COUNT(*) FROM time t WHERE t.start_time = ?"

# QUERY LISTS
create_table_queries = [
    user_table_create,
    songs_table_create,
    artist_table_create,
    time_table_create,
    songplay_table_create,
]
drop_table_queries = [
    user_table_drop,
    song_table_drop,
    artist_table_drop,
    time_table_drop,
    songplay_table_drop,
]
