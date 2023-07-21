#!/usr/bin/python3
from flask import Flask, request, jsonify, render_template, session
import sqlite3

app = Flask(__name__)


def create_db():
    """Create the SQLite3 database and table if they don't exist."""
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS messages 
                 (id INTEGER PRIMARY KEY, content TEXT)''')
    conn.commit()
    conn.close()


# Dummy data for demonstration purposes
herodata = [{
    "name": "Spider-Man",
    "realName": "Peter Parker",
    "since": 1962,
    "powers": [
        "wall crawling",
        "web shooters",
        "spider senses",
        "super human strength & agility"
    ]
}]

create_db()


@app.route('/herodata', methods=['GET'])
def get_hero_data():
    """Endpoint to return JSON data containing hero information."""
    return jsonify(herodata)


@app.route('/greet/<name>', methods=['GET'])
def greet_hero(name):
    """Endpoint to return HTML with a personalized greeting to a hero."""
    return render_template('greeting.html', name=name)


@app.route('/counter', methods=['GET'])
def counter():
    """Endpoint that reads from/writes to a cookie to count the visits."""
    count = request.cookies.get('count', 0)
    count = int(count) + 1
    resp = jsonify(message="Counter updated!")
    resp.set_cookie('count', str(count))
    return resp


if __name__ == '__main__':
    app.run(debug=True)

