# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/artists')
def list_artists():
    return render_template('artist.html')


@app.route("/albuns")
def list_albuns():
    pass


@app.route("/<artist>")
def list_artist(artist):
    pass


@app.route("/<artist>/<album>")
def list_artist_album(artist, album):
    pass


@app.route("/<genre>")
def list_genre(genre):
    pass