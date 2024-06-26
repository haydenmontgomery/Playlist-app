"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Playlist(db.Model):
    """Playlist."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = 'playlists'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.Text, nullable=False)

    description = db.Column(db.Text, nullable=False)
    
    #song_list = db.relationship('PlaylistSong', backref='playlist')

    #songs = db.relationship('PlaylistSong', backref='playlist')

class Song(db.Model):
    """Song."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    title = db.Column(db.Text, nullable=False)

    artist = db.Column(db.Text, nullable=False)

    #playlists = db.relationship('PlaylistSong', backref='song')

    # new try
    assigned_playlists = db.relationship('PlaylistSong', backref="song")

    playlists = db.relationship('Playlist', secondary='playlists_songs', backref='songs')

class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = 'playlists_songs'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey("playlists.id", ondelete='CASCADE'), primary_key = True)
    song_id = db.Column(db.Integer, db.ForeignKey("songs.id", ondelete='CASCADE'), primary_key = True)  

# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
