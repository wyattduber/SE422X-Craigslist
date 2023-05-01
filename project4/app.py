from flask import Flask, jsonify, request, make_response, url_for, session
from flask import render_template, redirect
import os
import MySQLdb
import MySQLdb.cursors
import re

from sections.config import DB_HOSTNAME, DB_USERNAME, DB_PASSWORD, DB_NAME

app = Flask(__name__, static_url_path="")
app.config.update(SECRET_KEY=os.urandom(24))

import sections.forsale
import sections.housing
import sections.services
import sections.jobs
import sections.community

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# Home Page
@app.route('/', methods=['GET', 'POST'])
def home():
    inSession = None
    if 'loggedin' in session:
        inSession = session['username']
    return render_template('home.html', inSession=inSession)

# Login functionality
@app.route('/login', methods=['GET', 'POST'])
def login():
    loginMsg = ''
    conn = MySQLdb.connect(host=DB_HOSTNAME,
                           user=DB_USERNAME,
                           passwd=DB_PASSWORD,
                           db=DB_NAME,
                           port=3306)
    cursor = conn.cursor()

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor.execute(
            f'SELECT * FROM {DB_NAME}.UserData WHERE username=%s AND password=%s', (username, password))
        record = cursor.fetchone()
        if record:
            session['loggedin'] = True
            session['username'] = record[0]
            loginMsg = 'Logged in succeessfully!'
        elif username == '' or password == '':
            loginMsg = 'Please fill in the fields completely.'
        else:
            loginMsg = 'Incorrect username/password. Try again.'

    inSession = None
    if 'loggedin' in session:
        inSession = session['username']

    return render_template('home.html', loginMsg=loginMsg, inSession=inSession)

# Sign Up functionality
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    signupMsg = ''
    conn = MySQLdb.connect(host=DB_HOSTNAME,
                           user=DB_USERNAME,
                           passwd=DB_PASSWORD,
                           db=DB_NAME,
                           port=3306)
    cursor = conn.cursor()

    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['pword']
        confirmPassword = request.form['cpword']
        if username == '' or password == '' or confirmPassword == '':
            signupMsg = 'Please fill out the sign up form completely!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            signupMsg = 'Username must contain only characters and numbers!'
        elif not password == confirmPassword:
            signupMsg = 'Passwords do not match!'
        else:
            cursor.execute(
                f"INSERT INTO {DB_NAME}.UserData (username, password) VALUES (%s,%s)", (username, password))
            conn.commit()
            conn.close()
            signupMsg = 'Signed up successfully!'
    else:
        signupMsg = 'Passwords do not match or you are missing fields. Try again.'

    return render_template('home.html', signupMsg=signupMsg)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)

    return redirect(url_for('login'))

@app.route('/jobs', methods=['GET'])
def jobs():
    return render_template('jobs.html')


@app.route('/housing', methods=['GET'])
def housing():
    return render_template('housing.html')


@app.route('/for-sale', methods=['GET'])
def sales():
    return render_template('forsale.html')


@app.route('/services', methods=['GET'])
def services():
    return render_template('services.html')


@app.route('/community', methods=['GET'])
def community():
    return render_template('community.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
