# a basic flask app with a form that inputs username and password and checks if the user is in the database, then logs them in

import os
import sqlite3
from flask import Flask, render_template, request, send_from_directory, session, redirect, url_for

app = Flask(__name__)
# set db as direct db connection
db = sqlite3.connect('temp.db')
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER,
        username TEXT,
        password TEXT
    )
''')
db.commit()
# add a user to the database
cursor.execute('INSERT INTO users VALUES(123, "admin", "password")')
db.commit()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # check if username and password are in the database
        db = sqlite3.connect('temp.db')
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'")
        user = cursor.fetchone()
        if user:
            return redirect(url_for('user', username=username))
    return f'<h2>Invalid username or password</h2>'

@app.route('/user/<username>')
def user(username):
    return f'<h1>Welcome {username}<h1>'

@app.route('/download/<path:filename>')
def file(filename):
    # Normalize the file path
    filename = os.path.normpath(filename)
    base_dir = app.root_path
    file_path = os.path.abspath(os.path.join(base_dir, filename))

    # Serve the requested file
    return send_from_directory(base_dir, filename)


if __name__ == '__main__':
    app.run(debug=True, port=6000)



# sneaky password: ' OR '1'='1
# tuples
