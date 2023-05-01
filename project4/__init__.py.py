import functions as db
from flask import Flask, jsonify, request, make_response, url_for, session
from flask import render_template, redirect
import os
import time
import datetime
import MySQLdb
import MySQLdb.cursors
import re

from sections.config import DB_HOSTNAME, DB_USERNAME, DB_PASSWORD, DB_NAME

app = Flask(__name__, static_url_path="")

import sections.forsale

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
            'SELECT * FROM DB_NAME.UserData WHERE username=%s AND password=%s', (username, password))
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


@app.route('/sales', methods=['GET'])
def sales():
    return render_template('sales.html')


@app.route('/services', methods=['GET'])
def services():
    return render_template('services.html')


@app.route('/community', methods=['GET'])
def community():
    return render_template('community.html')

# @app.route('/carTruck', methods=['GET', 'POST'])
# def carTruck():
    


@app.route('/boats', methods=['GET', 'POST'])
def boats():
    msg = ''
    inSession = None
    if 'loggedin' in session:
        inSession = session['username']
    else:
        msg = 'You can only view these options.'

    conn = MySQLdb.connect(host=DB_HOSTNAME,
                           user=DB_USERNAME,
                           passwd=DB_PASSWORD,
                           db=DB_NAME,
                           port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM DB_NAME.BoatData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        boat = {}
        boat['BoatID'] = item[0]
        boat['CreationTime'] = item[1]
        boat['Price'] = item[2]
        boat['Location'] = item[3]
        boat['PhoneNum'] = item[4]
        boat['BoatLength'] = item[5]
        boat['MakeModel'] = item[6]
        boat['YearBuilt'] = item[7]
        boat['BoatType'] = item[8]
        items.append(boat)
    conn.close()
    print(items)

    if request.method == 'POST':
        price = request.form['price']
        location = request.form['location']
        phoneNum = request.form['phoneNum']
        boat_length = request.form['boat_length']
        make_model = request.form['make_model']
        year_built = request.form['year_built']
        boat_type = request.form['boat_type']

        if price == '' or location == '' or phoneNum == '' or boat_length == '' or make_model == '' or year_built == '' or boat_type == '':
            msg = 'Make sure you filled our all the fields completely when uploading an item!'
        else:
            ts = time.time()
            timestamp = datetime.datetime.\
                fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

            conn = MySQLdb.connect(host=DB_HOSTNAME,
                                   user=DB_USERNAME,
                                   passwd=DB_PASSWORD,
                                   db=DB_NAME,
                                   port=3306)
            cursor = conn.cursor()

            statement = f"INSERT INTO {DB_NAME}.BoatData (creation_time, price, location, phoneNum, boat_length, make_model, year_built, boat_type) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        price+"', '" +\
                        location+"', '" +\
                        phoneNum+"', '" +\
                        boat_length+"', '" +\
                        make_model+"', '" +\
                        year_built+"', '" +\
                        boat_type+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()
            return redirect('/boats')
    else:
        msg = 'You can only view these options. Sign up or Login if you want to upload items!'
        # return render_template('carTruck.html')

    return render_template('/forSale/boats.html', inSession=inSession, boats=items, msg=msg)


@app.route('/books', methods=['GET', 'POST'])
def books():
    msg = ''
    inSession = None
    if 'loggedin' in session:
        inSession = session['username']
    else:
        msg = 'You can only view these options.'

    conn = MySQLdb.connect(host=DB_HOSTNAME,
                           user=DB_USERNAME,
                           passwd=DB_PASSWORD,
                           db=DB_NAME,
                           port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM DB_NAME.BookData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        book = {}
        book['BookID'] = item[0]
        book['CreationTime'] = item[1]
        book['Price'] = item[2]
        book['Location'] = item[3]
        book['PhoneNum'] = item[4]
        book['Author'] = item[5]
        book['BookType'] = item[6]
        book['Title'] = item[7]
        items.append(book)
    conn.close()
    print(items)

    if request.method == 'POST':
        price = request.form['price']
        location = request.form['location']
        phoneNum = request.form['phoneNum']
        author = request.form['author']
        book_type = request.form['bookType']
        title = request.form['title']

        if price == '' or location == '' or phoneNum == '' or author == '' or book_type == '' or title == '':
            msg = 'Make sure you filled our all the fields completely when uploading an item!'
        else:
            ts = time.time()
            timestamp = datetime.datetime.\
                fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

            conn = MySQLdb.connect(host=DB_HOSTNAME,
                                   user=DB_USERNAME,
                                   passwd=DB_PASSWORD,
                                   db=DB_NAME,
                                   port=3306)
            cursor = conn.cursor()

            statement = f"INSERT INTO {DB_NAME}.BookData (creation_time, price, location, phoneNum, author, book_type, title) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        price+"', '" +\
                        location+"', '" +\
                        phoneNum+"', '" +\
                        author+"', '" +\
                        book_type+"', '" +\
                        title+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/books')
    else:
        msg = 'You can only view these options. Sign up or Login if you want to upload items!'
    return render_template('/forSale/books.html', inSession=inSession, books=items, msg=msg)


@app.route('/furniture', methods=['GET', 'POST'])
def furniture():
    msg = ''
    inSession = None
    if 'loggedin' in session:
        inSession = session['username']
    else:
        msg = 'You can only view these options.'

    conn = MySQLdb.connect(host=DB_HOSTNAME,
                           user=DB_USERNAME,
                           passwd=DB_PASSWORD,
                           db=DB_NAME,
                           port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM DB_NAME.FurnitureData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        furniture = {}
        furniture['FurnitureID'] = item[0]
        furniture['CreationTime'] = item[1]
        furniture['Price'] = item[2]
        furniture['Location'] = item[3]
        furniture['PhoneNum'] = item[4]
        furniture['Brand'] = item[5]
        furniture['FurnitureType'] = item[6]
        items.append(furniture)
    conn.close()
    print(items)

    if request.method == 'POST':
        price = request.form['price']
        location = request.form['location']
        phoneNum = request.form['phoneNum']
        brand = request.form['brand']
        furniture_type = request.form['furniture_type']

        if price == '' or location == '' or phoneNum == '' or brand == '' or furniture_type == '':
            msg = 'Make sure you filled our all the fields completely when uploading an item!'
        else:
            ts = time.time()
            timestamp = datetime.datetime.\
                fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

            conn = MySQLdb.connect(host=DB_HOSTNAME,
                                   user=DB_USERNAME,
                                   passwd=DB_PASSWORD,
                                   db=DB_NAME,
                                   port=3306)
            cursor = conn.cursor()

            statement = f"INSERT INTO {DB_NAME}.FurnitureData (creation_time, price, location, phone_num, brand, furniture_type) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        price+"', '" +\
                        location+"', '" +\
                        phoneNum+"', '" +\
                        brand+"', '" +\
                        furniture_type+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/furniture')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/forSale/furniture.html', inSession=inSession, furnitures=items, msg=msg)


@app.route('/bikes', methods=['GET', 'POST'])
def bikes():
    msg = ''
    inSession = None
    if 'loggedin' in session:
        inSession = session['username']
    else:
        msg = 'You can only view these options.'

    conn = MySQLdb.connect(host=DB_HOSTNAME,
                           user=DB_USERNAME,
                           passwd=DB_PASSWORD,
                           db=DB_NAME,
                           port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM DB_NAME.BikeData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        bike = {}
        bike['BikeID'] = item[0]
        bike['CreationTime'] = item[1]
        bike['Price'] = item[2]
        bike['Location'] = item[3]
        bike['PhoneNum'] = item[4]
        bike['Bike_Type'] = item[5]
        bike['Color'] = item[6]
        items.append(bike)
    conn.close()
    print(items)

    if request.method == 'POST':
        price = request.form['price']
        location = request.form['location']
        phoneNum = request.form['phoneNum']
        bike_type = request.form['bike_type']
        color = request.form['color']

        if price == '' or location == '' or phoneNum == '' or bike_type == '' or color == '':
            msg = 'Make sure you filled our all the fields completely when uploading an item!'
        else:
            ts = time.time()
            timestamp = datetime.datetime.\
                fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

            conn = MySQLdb.connect(host=DB_HOSTNAME,
                                   user=DB_USERNAME,
                                   passwd=DB_PASSWORD,
                                   db=DB_NAME,
                                   port=3306)
            cursor = conn.cursor()

            statement = f"INSERT INTO {DB_NAME}.BikeData (creation_time, price, location, phoneNum, bike_type, color) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        price+"', '" +\
                        location+"', '" +\
                        phoneNum+"', '" +\
                        bike_type+"', '" +\
                        color+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/bikes')

    else:
        msg = 'You can only view these options. Sign up or Login if you want to upload items!'
        # return render_template('carTruck.html')

    return render_template('/forSale/bikes.html', inSession=inSession, bikes=items, msg=msg)

#-------------------------------- LINKS FOR HOUSING ITEMS --------------------------------#


@app.route('/apartments', methods=['GET', 'POST'])
def apartments():
    msg = ''
    inSession = None
    if 'loggedin' in session:
        inSession = session['username']
    else:
        msg = 'You can only view these options.'

    conn = MySQLdb.connect(host=DB_HOSTNAME,
                           user=DB_USERNAME,
                           passwd=DB_PASSWORD,
                           db=DB_NAME,
                           port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM DB_NAME.ApartmentData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        apartment = {}
        apartment['ApartmentID'] = item[0]
        apartment['CreationTime'] = item[1]
        apartment['Location'] = item[2]
        apartment['PhoneNum'] = item[3]
        apartment['Rent'] = item[4]
        apartment['SquareFeet'] = item[5]
        apartment['NumBathrooms'] = item[6]
        apartment['NumBedrooms'] = item[7]
        items.append(apartment)
    conn.close()
    print(items)

    if request.method == 'POST':
        rent = request.form['rent']
        location = request.form['location']
        phoneNum = request.form['phoneNum']
        square_feet = request.form['square_feet']
        num_bathrooms = request.form['num_bathrooms']
        num_bedrooms = request.form['num_bedrooms']

        if rent == '' or location == '' or phoneNum == '' or square_feet == '' or num_bathrooms == '' or num_bedrooms == '':
            msg = 'Make sure you filled our all the fields completely when uploading an item!'
        else:
            ts = time.time()
            timestamp = datetime.datetime.\
                fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

            conn = MySQLdb.connect(host=DB_HOSTNAME,
                                   user=DB_USERNAME,
                                   passwd=DB_PASSWORD,
                                   db=DB_NAME,
                                   port=3306)
            cursor = conn.cursor()

            statement = f"INSERT INTO {DB_NAME}.ApartmentData (creation_time, location, phone_num, rent, square_feet, num_bathrooms, num_bedrooms) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phoneNum+"', '" +\
                        rent+"', '" +\
                        square_feet+"', '" +\
                        num_bathrooms+"', '" +\
                        num_bedrooms+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()
            return redirect('/apartments')

    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/housingItems/apartments.html', inSession=inSession, apartments=items, msg=msg)


@app.route('/offices', methods=['GET', 'POST'])
def offices():
    msg = ''
    inSession = None
    if 'loggedin' in session:
        inSession = session['username']
    else:
        msg = 'You can only view these options.'

    conn = MySQLdb.connect(host=DB_HOSTNAME,
                           user=DB_USERNAME,
                           passwd=DB_PASSWORD,
                           db=DB_NAME,
                           port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM DB_NAME.OfficesData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        office = {}
        office['OfficesID'] = item[0]
        office['CreationTime'] = item[1]
        office['Location'] = item[2]
        office['PhoneNum'] = item[3]
        office['Rent'] = item[4]
        office['SquareFeet'] = item[5]
        office['NumRooms'] = item[6]
        items.append(office)
    conn.close()
    print(items)

    if request.method == 'POST':
        rent = request.form['rent']
        location = request.form['location']
        phoneNum = request.form['phoneNum']
        square_feet = request.form['square_feet']
        num_rooms = request.form['num_rooms']

        if rent == '' or location == '' or phoneNum == '' or square_feet == '' or num_rooms == '':
            msg = 'Make sure you filled our all the fields completely when uploading an item!'
        else:
            ts = time.time()
            timestamp = datetime.datetime.\
                fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

            conn = MySQLdb.connect(host=DB_HOSTNAME,
                                   user=DB_USERNAME,
                                   passwd=DB_PASSWORD,
                                   db=DB_NAME,
                                   port=3306)
            cursor = conn.cursor()

            statement = f"INSERT INTO {DB_NAME}.OfficesData (creation_time, location, phone_num, rent, square_feet, num_rooms) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phoneNum+"', '" +\
                        rent+"', '" +\
                        square_feet+"', '" +\
                        num_rooms+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/offices')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/housingItems/offices.html', inSession=inSession, offices=items, msg=msg)


@app.route('/realEstate', methods=['GET', 'POST'])
def realEstate():
    msg = ''
    inSession = None
    if 'loggedin' in session:
        inSession = session['username']
    else:
        msg = 'You can only view these options.'

    conn = MySQLdb.connect(host=DB_HOSTNAME,
                           user=DB_USERNAME,
                           passwd=DB_PASSWORD,
                           db=DB_NAME,
                           port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM DB_NAME.RealEstateData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        realEstate = {}
        realEstate['RealEstateID'] = item[0]
        realEstate['CreationTime'] = item[1]
        realEstate['Location'] = item[2]
        realEstate['PhoneNum'] = item[3]
        realEstate['Cost'] = item[4]
        realEstate['SquareFeet'] = item[5]
        realEstate['NumBathrooms'] = item[6]
        realEstate['NumBedrooms'] = item[7]
        items.append(realEstate)
    conn.close()
    print(items)

    if request.method == 'POST':
        cost = request.form['cost']
        location = request.form['location']
        phoneNum = request.form['phoneNum']
        square_feet = request.form['square_feet']
        num_bathrooms = request.form['num_bathrooms']
        num_bedrooms = request.form['num_bedrooms']

        if cost == '' or location == '' or phoneNum == '' or square_feet == '' or num_bathrooms == '' or num_bedrooms == '':
            msg = 'Make sure you filled our all the fields completely when uploading an item!'
        else:
            ts = time.time()
            timestamp = datetime.datetime.\
                fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

            conn = MySQLdb.connect(host=DB_HOSTNAME,
                                   user=DB_USERNAME,
                                   passwd=DB_PASSWORD,
                                   db=DB_NAME,
                                   port=3306)
            cursor = conn.cursor()

            statement = f"INSERT INTO {DB_NAME}.RealEstateData (creation_time, location, phone_num, cost, square_feet, num_bathrooms, num_bedrooms) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phoneNum+"', '" +\
                        cost+"', '" +\
                        square_feet+"', '" +\
                        num_bathrooms+"', '" +\
                        num_bedrooms+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/realEstate')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/housingItems/realEstate.html', inSession=inSession, realEstates=items, msg=msg)


@app.route('/rooms', methods=['GET', 'POST'])
def rooms():
    msg = None
    inSession = None
    if 'loggedin' in session:
        inSession = session['username']
    else:
        msg = 'You can only view these options. Sign up or Login if you want to upload items!'

    conn = MySQLdb.connect(host=DB_HOSTNAME,
                           user=DB_USERNAME,
                           passwd=DB_PASSWORD,
                           db=DB_NAME,
                           port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM DB_NAME.RoomsData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        room = {}
        room['RoomsID'] = item[0]
        room['CreationTime'] = item[1]
        room['Location'] = item[2]
        room['PhoneNum'] = item[3]
        room['Rent'] = item[4]
        room['SquareFeet'] = item[5]
        items.append(room)
    conn.close()
    print(items)

    if request.method == 'POST':
        rent = request.form['rent']
        location = request.form['location']
        phoneNum = request.form['phoneNum']
        square_feet = request.form['square_feet']

        if rent == '' or location == '' or phoneNum == '' or square_feet == '':
            msg = 'Make sure you filled our all the fields completely when uploading an item!'
        else:
            ts = time.time()
            timestamp = datetime.datetime.\
                fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

            conn = MySQLdb.connect(host=DB_HOSTNAME,
                                   user=DB_USERNAME,
                                   passwd=DB_PASSWORD,
                                   db=DB_NAME,
                                   port=3306)
            cursor = conn.cursor()

            statement = f"INSERT INTO {DB_NAME}.RoomsData (creation_time, location, phone_num, rent, square_feet) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phoneNum+"', '" +\
                        rent+"', '" +\
                        square_feet+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()
            return redirect('/rooms')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/housingItems/rooms.html', inSession=inSession, rooms=items, msg=msg)


@app.route('/vacation', methods=['GET', 'POST'])
def vacation():
    msg = None
    inSession = None
    if 'loggedin' in session:
        inSession = session['username']
    else:
        msg = 'You can only view these options. Sign up or Login if you want to upload items!'

    conn = MySQLdb.connect(host=DB_HOSTNAME,
                           user=DB_USERNAME,
                           passwd=DB_PASSWORD,
                           db=DB_NAME,
                           port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM DB_NAME.VacationData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        vacation = {}
        vacation['VacationID'] = item[0]
        vacation['CreationTime'] = item[1]
        vacation['Location'] = item[2]
        vacation['PhoneNum'] = item[3]
        vacation['CostPerNight'] = item[4]
        vacation['NumBeds'] = item[5]
        items.append(vacation)
    conn.close()
    print(items)

    if request.method == 'POST':
        location = request.form['location']
        phoneNum = request.form['phoneNum']
        cost_per_night = request.form['cost_per_night']
        num_beds = request.form['num_beds']

        if cost_per_night == '' or location == '' or phoneNum == '' or num_beds == '':
            msg = 'Make sure you filled our all the fields completely when uploading an item!'
        else:
            ts = time.time()
            timestamp = datetime.datetime.\
                fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

            conn = MySQLdb.connect(host=DB_HOSTNAME,
                                   user=DB_USERNAME,
                                   passwd=DB_PASSWORD,
                                   db=DB_NAME,
                                   port=3306)
            cursor = conn.cursor()

            statement = f"INSERT INTO {DB_NAME}.VacationData (creation_time, location, phone_num, cost_per_night, num_beds) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phoneNum+"', '" +\
                        cost_per_night+"', '" +\
                        num_beds+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/vacation')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/housingItems/vacation.html', inSession=inSession, vacations=items, msg=msg)

#-------------------------------- LINKS FOR SERVICE ITEMS --------------------------------#


@app.route('/automotive', methods=['GET', 'POST'])
def automotive():
    msg = ''
    inSession = None
    if 'loggedin' in session:
        inSession = session['username']
    else:
        msg = 'You can only view these options.'

    conn = MySQLdb.connect(host=DB_HOSTNAME,
                           user=DB_USERNAME,
                           passwd=DB_PASSWORD,
                           db=DB_NAME,
                           port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM DB_NAME.AutomotiveData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        automotive = {}
        automotive['AutomativeID'] = item[0]
        automotive['CreationTime'] = item[1]
        automotive['Location'] = item[2]
        automotive['PhoneNum'] = item[3]
        automotive['Cost'] = item[4]
        automotive['OperatingHours'] = item[5]
        automotive['Duration'] = item[6]
        automotive['Reservation'] = item[7]
        items.append(automotive)
    conn.close()
    print(items)

    if request.method == 'POST':
        cost = request.form['cost']
        location = request.form['location']
        phoneNum = request.form['phoneNum']
        operating_hours = request.form['operating_hours']
        duration = request.form['duration']
        reservation = request.form['reservation']

        if cost == '' or location == '' or phoneNum == '' or operating_hours == '' or duration == '' or reservation == '':
            msg = 'Make sure you filled our all the fields completely when uploading an item!'
        else:
            ts = time.time()
            timestamp = datetime.datetime.\
                fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

            conn = MySQLdb.connect(host=DB_HOSTNAME,
                                   user=DB_USERNAME,
                                   passwd=DB_PASSWORD,
                                   db=DB_NAME,
                                   port=3306)
            cursor = conn.cursor()

            statement = f"INSERT INTO {DB_NAME}.AutomotiveData (creation_time, location, phone_num, cost, operating_hours, duration, reservation) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phoneNum+"', '" +\
                        cost+"', '" +\
                        operating_hours+"', '" +\
                        duration+"', '" +\
                        reservation+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()
            return redirect('/automotive')
    else:
        msg = 'You can only view these options. Sign up or Login if you want to upload items!'

    return render_template('/serviceItems/automotive.html', inSession=inSession, automotive=items, msg=msg)


@app.route('/computer', methods=['GET', 'POST'])
def computer():
    msg = ''
    inSession = None
    if 'loggedin' in session:
        inSession = session['username']
    else:
        msg = 'You can only view these options.'

    conn = MySQLdb.connect(host=DB_HOSTNAME,
                           user=DB_USERNAME,
                           passwd=DB_PASSWORD,
                           db=DB_NAME,
                           port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM DB_NAME.ComputerData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        computer = {}
        computer['ComputerID'] = item[0]
        computer['CreationTime'] = item[1]
        computer['Location'] = item[2]
        computer['PhoneNum'] = item[3]
        computer['Cost'] = item[4]
        computer['OperatingHours'] = item[5]
        computer['Reservation'] = item[6]
        items.append(computer)
    conn.close()
    print(items)

    if request.method == 'POST':
        cost = request.form['cost']
        location = request.form['location']
        phoneNum = request.form['phoneNum']
        operating_hours = request.form['operating_hours']
        reservation = request.form['reservation']

        if cost == '' or location == '' or phoneNum == '' or operating_hours == '' or reservation == '':
            msg = 'Make sure you filled our all the fields completely when uploading an item!'
        else:
            ts = time.time()
            timestamp = datetime.datetime.\
                fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

            conn = MySQLdb.connect(host=DB_HOSTNAME,
                                   user=DB_USERNAME,
                                   passwd=DB_PASSWORD,
                                   db=DB_NAME,
                                   port=3306)
            cursor = conn.cursor()

            statement = f"INSERT INTO {DB_NAME}.ComputerData (creation_time, location, phone_num, cost, operating_hours, reservation) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phoneNum+"', '" +\
                        cost+"', '" +\
                        operating_hours+"', '" +\
                        reservation+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()
            return redirect('/computer')
    else:
        msg = 'You can only view these options. Sign up or Login if you want to upload items!'

    return render_template('/serviceItems/computer.html', inSession=inSession, computer=items, msg=msg)


@app.route('/legal', methods=['GET', 'POST'])
def legal():
    msg = ''
    inSession = None
    if 'loggedin' in session:
        inSession = session['username']
    else:
        msg = 'You can only view these options.'

    conn = MySQLdb.connect(host=DB_HOSTNAME,
                           user=DB_USERNAME,
                           passwd=DB_PASSWORD,
                           db=DB_NAME,
                           port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM DB_NAME.LegalData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        legal = {}
        legal['LegalID'] = item[0]
        legal['CreationTime'] = item[1]
        legal['Location'] = item[2]
        legal['PhoneNum'] = item[3]
        legal['Cost'] = item[4]
        legal['OperatingHours'] = item[5]
        legal['Reservation'] = item[6]
        items.append(legal)
    conn.close()
    print(items)

    if request.method == 'POST':
        cost = request.form['cost']
        location = request.form['location']
        phoneNum = request.form['phoneNum']
        operating_hours = request.form['operating_hours']
        reservation = request.form['reservation']

        if cost == '' or location == '' or phoneNum == '' or operating_hours == '' or reservation == '':
            msg = 'Make sure you filled our all the fields completely when uploading an item!'
        else:
            ts = time.time()
            timestamp = datetime.datetime.\
                fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

            conn = MySQLdb.connect(host=DB_HOSTNAME,
                                   user=DB_USERNAME,
                                   passwd=DB_PASSWORD,
                                   db=DB_NAME,
                                   port=3306)
            cursor = conn.cursor()

            statement = f"INSERT INTO {DB_NAME}.LegalData (creation_time, location, phone_num, cost, operating_hours, reservation) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phoneNum+"', '" +\
                        cost+"', '" +\
                        operating_hours+"', '" +\
                        reservation+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/legal')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/serviceItems/legal.html', inSession=inSession, legal=items, msg=msg)


@app.route('/movingLabor', methods=['GET', 'POST'])
def movingLabor():
    msg = ''
    inSession = None
    if 'loggedin' in session:
        inSession = session['username']
    else:
        msg = 'You can only view these options.'

    conn = MySQLdb.connect(host=DB_HOSTNAME,
                           user=DB_USERNAME,
                           passwd=DB_PASSWORD,
                           db=DB_NAME,
                           port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM DB_NAME.MovingLaborData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        movingLabor = {}
        movingLabor['MovingLaborID'] = item[0]
        movingLabor['CreationTime'] = item[1]
        movingLabor['Location'] = item[2]
        movingLabor['PhoneNum'] = item[3]
        movingLabor['Cost'] = item[4]
        movingLabor['OperatingHours'] = item[5]
        movingLabor['Reservation'] = item[6]
        items.append(movingLabor)
    conn.close()
    print(items)

    if request.method == 'POST':
        cost = request.form['cost']
        location = request.form['location']
        phoneNum = request.form['phoneNum']
        operating_hours = request.form['operating_hours']
        reservation = request.form['reservation']

        if cost == '' or location == '' or phoneNum == '' or operating_hours == '' or reservation == '':
            msg = 'Make sure you filled our all the fields completely when uploading an item!'
        else:
            ts = time.time()
            timestamp = datetime.datetime.\
                fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

            conn = MySQLdb.connect(host=DB_HOSTNAME,
                                   user=DB_USERNAME,
                                   passwd=DB_PASSWORD,
                                   db=DB_NAME,
                                   port=3306)
            cursor = conn.cursor()

            statement = f"INSERT INTO {DB_NAME}.MovingLaborData (creation_time, location, phone_num, cost, operating_hours, reservation) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phoneNum+"', '" +\
                        cost+"', '" +\
                        operating_hours+"', '" +\
                        reservation+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/movingLabor')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/serviceItems/movingLabor.html', inSession=inSession, movingLabor=items, msg=msg)


@app.route('/farm', methods=['GET', 'POST'])
def farm():
    msg = ''
    inSession = None
    if 'loggedin' in session:
        inSession = session['username']
    else:
        msg = 'You can only view these options.'

    conn = MySQLdb.connect(host=DB_HOSTNAME,
                           user=DB_USERNAME,
                           passwd=DB_PASSWORD,
                           db=DB_NAME,
                           port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM DB_NAME.FarmData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        farm = {}
        farm['FarmID'] = item[0]
        farm['CreationTime'] = item[1]
        farm['Location'] = item[2]
        farm['PhoneNum'] = item[3]
        farm['Cost'] = item[4]
        farm['OperatingHours'] = item[5]
        farm['Reservation'] = item[6]
        items.append(farm)
    conn.close()
    print(items)

    if request.method == 'POST':
        cost = request.form['cost']
        location = request.form['location']
        phoneNum = request.form['phoneNum']
        operating_hours = request.form['operating_hours']
        reservation = request.form['reservation']

        if cost == '' or location == '' or phoneNum == '' or operating_hours == '' or reservation == '':
            msg = 'Make sure you filled our all the fields completely when uploading an item!'
        else:
            ts = time.time()
            timestamp = datetime.datetime.\
                fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

            conn = MySQLdb.connect(host=DB_HOSTNAME,
                                   user=DB_USERNAME,
                                   passwd=DB_PASSWORD,
                                   db=DB_NAME,
                                   port=3306)
            cursor = conn.cursor()

            statement = f"INSERT INTO {DB_NAME}.FarmData (creation_time, location, phone_num, cost, operating_hours, reservation) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phoneNum+"', '" +\
                        cost+"', '" +\
                        operating_hours+"', '" +\
                        reservation+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/farm')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/serviceItems/farm.html', inSession=inSession, farm=items, msg=msg)

#-------------------------------- LINKS FOR JOB ITEMS --------------------------------#


@app.route('/accounting', methods=['GET', 'POST'])
def accounting():
    msg = ''
    inSession = None
    if 'loggedin' in session:
        inSession = session['username']
    else:
        msg = 'You can only view these options.'

    conn = MySQLdb.connect(host=DB_HOSTNAME,
                           user=DB_USERNAME,
                           passwd=DB_PASSWORD,
                           db=DB_NAME,
                           port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM DB_NAME.AccountingData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        accounting = {}
        accounting['AccountingID'] = item[0]
        accounting['CreationTime'] = item[1]
        accounting['Location'] = item[2]
        accounting['PhoneNum'] = item[3]
        accounting['Salary'] = item[4]
        accounting['Experience'] = item[5]
        accounting['RemotePerson'] = item[6]
        accounting['Title'] = item[7]
        accounting['CompanyName'] = item[8]
        items.append(accounting)
    conn.close()
    print(items)

    if request.method == 'POST':
        salary = request.form['salary']
        location = request.form['location']
        phoneNum = request.form['phoneNum']
        experience = request.form['experience']
        remote_person = request.form['remote_person']
        title = request.form['title']
        company_name = request.form['company_name']

        if salary == '' or location == '' or phoneNum == '' or experience == '' or remote_person == '' or title == '' or company_name == '':
            msg = 'Make sure you filled our all the fields completely when uploading an item!'
        else:
            ts = time.time()
            timestamp = datetime.datetime.\
                fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

            conn = MySQLdb.connect(host=DB_HOSTNAME,
                                   user=DB_USERNAME,
                                   passwd=DB_PASSWORD,
                                   db=DB_NAME,
                                   port=3306)
            cursor = conn.cursor()

            statement = f"INSERT INTO {DB_NAME}.AccountingData (creation_time, location, phone_num, salary, experience, remote_person, title, company_name) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phoneNum+"', '" +\
                        salary+"', '" +\
                        experience+"', '" +\
                        remote_person+"', '" +\
                        title+"', '" +\
                        company_name+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/accounting')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/jobItems/accounting.html', inSession=inSession, accounting=items, msg=msg)


@app.route('/education', methods=['GET', 'POST'])
def education():
    msg = ''
    inSession = None
    if 'loggedin' in session:
        inSession = session['username']
    else:
        msg = 'You can only view these options.'

    conn = MySQLdb.connect(host=DB_HOSTNAME,
                           user=DB_USERNAME,
                           passwd=DB_PASSWORD,
                           db=DB_NAME,
                           port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM DB_NAME.EducationData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        education = {}
        education['AccountingID'] = item[0]
        education['CreationTime'] = item[1]
        education['Location'] = item[2]
        education['PhoneNum'] = item[3]
        education['Salary'] = item[4]
        education['Experience'] = item[5]
        education['RemotePerson'] = item[6]
        education['Title'] = item[7]
        education['CompanyName'] = item[8]
        items.append(education)
    conn.close()
    print(items)

    if request.method == 'POST':
        salary = request.form['salary']
        location = request.form['location']
        phoneNum = request.form['phoneNum']
        experience = request.form['experience']
        remote_person = request.form['remote_person']
        title = request.form['title']
        company_name = request.form['company_name']

        if salary == '' or location == '' or phoneNum == '' or experience == '' or remote_person == '' or title == '' or company_name == '':
            msg = 'Make sure you filled our all the fields completely when uploading an item!'
        else:
            ts = time.time()
            timestamp = datetime.datetime.\
                fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

            conn = MySQLdb.connect(host=DB_HOSTNAME,
                                   user=DB_USERNAME,
                                   passwd=DB_PASSWORD,
                                   db=DB_NAME,
                                   port=3306)
            cursor = conn.cursor()

            statement = f"INSERT INTO {DB_NAME}.EducationData (creation_time, location, phone_num, salary, experience, remote_person, title, company_name) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phoneNum+"', '" +\
                        salary+"', '" +\
                        experience+"', '" +\
                        remote_person+"', '" +\
                        title+"', '" +\
                        company_name+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/education')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/jobItems/education.html', inSession=inSession, education=items, msg=msg)


@app.route('/engineering', methods=['GET', 'POST'])
def engineering():
    msg = ''
    inSession = None
    if 'loggedin' in session:
        inSession = session['username']
    else:
        msg = 'You can only view these options.'

    conn = MySQLdb.connect(host=DB_HOSTNAME,
                           user=DB_USERNAME,
                           passwd=DB_PASSWORD,
                           db=DB_NAME,
                           port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM DB_NAME.EngineeringData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        engineering = {}
        engineering['AccountingID'] = item[0]
        engineering['CreationTime'] = item[1]
        engineering['Location'] = item[2]
        engineering['PhoneNum'] = item[3]
        engineering['Salary'] = item[4]
        engineering['Experience'] = item[5]
        engineering['RemotePerson'] = item[6]
        engineering['Title'] = item[7]
        engineering['CompanyName'] = item[8]
        items.append(engineering)
    conn.close()
    print(items)

    if request.method == 'POST':
        salary = request.form['salary']
        location = request.form['location']
        phoneNum = request.form['phoneNum']
        experience = request.form['experience']
        remote_person = request.form['remote_person']
        title = request.form['title']
        company_name = request.form['company_name']

        if salary == '' or location == '' or phoneNum == '' or experience == '' or remote_person == '' or title == '' or company_name == '':
            msg = 'Make sure you filled our all the fields completely when uploading an item!'
        else:
            ts = time.time()
            timestamp = datetime.datetime.\
                fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

            conn = MySQLdb.connect(host=DB_HOSTNAME,
                                   user=DB_USERNAME,
                                   passwd=DB_PASSWORD,
                                   db=DB_NAME,
                                   port=3306)
            cursor = conn.cursor()

            statement = f"INSERT INTO {DB_NAME}.EngineeringData (creation_time, location, phone_num, salary, experience, remote_person, title, company_name) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phoneNum+"', '" +\
                        salary+"', '" +\
                        experience+"', '" +\
                        remote_person+"', '" +\
                        title+"', '" +\
                        company_name+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/engineering')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/jobItems/engineering.html', inSession=inSession, engineering=items, msg=msg)


@app.route('/labor', methods=['GET', 'POST'])
def labor():
    msg = ''
    inSession = None
    if 'loggedin' in session:
        inSession = session['username']
    else:
        msg = 'You can only view these options.'

    conn = MySQLdb.connect(host=DB_HOSTNAME,
                           user=DB_USERNAME,
                           passwd=DB_PASSWORD,
                           db=DB_NAME,
                           port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM DB_NAME.LaborData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        labor = {}
        labor['AccountingID'] = item[0]
        labor['CreationTime'] = item[1]
        labor['Location'] = item[2]
        labor['PhoneNum'] = item[3]
        labor['Salary'] = item[4]
        labor['Experience'] = item[5]
        labor['RemotePerson'] = item[6]
        labor['Title'] = item[7]
        labor['CompanyName'] = item[8]
        items.append(labor)
    conn.close()
    print(items)

    if request.method == 'POST':
        salary = request.form['salary']
        location = request.form['location']
        phoneNum = request.form['phoneNum']
        experience = request.form['experience']
        remote_person = request.form['remote_person']
        title = request.form['title']
        company_name = request.form['company_name']

        if salary == '' or location == '' or phoneNum == '' or experience == '' or remote_person == '' or title == '' or company_name == '':
            msg = 'Make sure you filled our all the fields completely when uploading an item!'
        else:
            ts = time.time()
            timestamp = datetime.datetime.\
                fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

            conn = MySQLdb.connect(host=DB_HOSTNAME,
                                   user=DB_USERNAME,
                                   passwd=DB_PASSWORD,
                                   db=DB_NAME,
                                   port=3306)
            cursor = conn.cursor()

            statement = f"INSERT INTO {DB_NAME}.LaborData (creation_time, location, phone_num, salary, experience, remote_person, title, company_name) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phoneNum+"', '" +\
                        salary+"', '" +\
                        experience+"', '" +\
                        remote_person+"', '" +\
                        title+"', '" +\
                        company_name+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/labor')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/jobItems/labor.html', inSession=inSession, labor=items, msg=msg)


@app.route('/retail', methods=['GET', 'POST'])
def retail():
    msg = ''
    inSession = None
    if 'loggedin' in session:
        inSession = session['username']
    else:
        msg = 'You can only view these options.'

    conn = MySQLdb.connect(host=DB_HOSTNAME,
                           user=DB_USERNAME,
                           passwd=DB_PASSWORD,
                           db=DB_NAME,
                           port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM DB_NAME.RetailData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        retail = {}
        retail['AccountingID'] = item[0]
        retail['CreationTime'] = item[1]
        retail['Location'] = item[2]
        retail['PhoneNum'] = item[3]
        retail['Salary'] = item[4]
        retail['Experience'] = item[5]
        retail['RemotePerson'] = item[6]
        retail['Title'] = item[7]
        retail['CompanyName'] = item[8]
        items.append(retail)
    conn.close()
    print(items)

    if request.method == 'POST':
        salary = request.form['salary']
        location = request.form['location']
        phoneNum = request.form['phoneNum']
        experience = request.form['experience']
        remote_person = request.form['remote_person']
        title = request.form['title']
        company_name = request.form['company_name']

        if salary == '' or location == '' or phoneNum == '' or experience == '' or remote_person == '' or title == '' or company_name == '':
            msg = 'Make sure you filled our all the fields completely when uploading an item!'
        else:
            ts = time.time()
            timestamp = datetime.datetime.\
                fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

            conn = MySQLdb.connect(host=DB_HOSTNAME,
                                   user=DB_USERNAME,
                                   passwd=DB_PASSWORD,
                                   db=DB_NAME,
                                   port=3306)
            cursor = conn.cursor()

            statement = f"INSERT INTO {DB_NAME}.RetailData (creation_time, location, phone_num, salary, experience, remote_person, title, company_name) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phoneNum+"', '" +\
                        salary+"', '" +\
                        experience+"', '" +\
                        remote_person+"', '" +\
                        title+"', '" +\
                        company_name+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/retail')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/jobItems/retail.html', inSession=inSession, retail=items, msg=msg)

#-------------------------------- LINKS FOR COMMUNITY ITEMS --------------------------------#


@app.route('/activities', methods=['GET', 'POST'])
def activities():
    msg = ''
    inSession = None
    if 'loggedin' in session:
        inSession = session['username']
    else:
        msg = 'You can only view these options.'

    conn = MySQLdb.connect(host=DB_HOSTNAME,
                           user=DB_USERNAME,
                           passwd=DB_PASSWORD,
                           db=DB_NAME,
                           port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM DB_NAME.ActivitiesData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        activity = {}
        activity['ActivityID'] = item[0]
        activity['CreationTime'] = item[1]
        activity['Location'] = item[2]
        activity['PhoneNum'] = item[3]
        activity['AgeGroup'] = item[4]
        activity['TimeDate'] = item[5]
        activity['Title'] = item[6]

        items.append(activity)
    conn.close()
    print(items)

    if request.method == 'POST':
        location = request.form['location']
        phone_num = request.form['phone_num']
        age_group = request.form['age_group']
        time_date = request.form['time_date']
        title = request.form['title']

        if location == '' or phoneNum == '' or age_group == '' or time_date == '' or title == '':
            msg = 'Make sure you filled our all the fields completely when uploading an item!'
        else:
            ts = time.time()
            timestamp = datetime.datetime.\
                fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

            conn = MySQLdb.connect(host=DB_HOSTNAME,
                                   user=DB_USERNAME,
                                   passwd=DB_PASSWORD,
                                   db=DB_NAME,
                                   port=3306)
            cursor = conn.cursor()

            statement = f"INSERT INTO {DB_NAME}.ActivitiesData (creation_time, location, phone_num, age_group, time_date, title) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phone_num+"', '" +\
                        age_group+"', '" +\
                        time_date+"', '" +\
                        title+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/activities')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/communityItems/activities.html', inSession=inSession, activities=items, msg=msg)


@app.route('/childcare', methods=['GET', 'POST'])
def childcare():
    msg = ''
    inSession = None
    if 'loggedin' in session:
        inSession = session['username']
    else:
        msg = 'You can only view these options.'

    conn = MySQLdb.connect(host=DB_HOSTNAME,
                           user=DB_USERNAME,
                           passwd=DB_PASSWORD,
                           db=DB_NAME,
                           port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM DB_NAME.ChildCareData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        child_care = {}
        child_care['ChildCareID'] = item[0]
        child_care['CreationTime'] = item[1]
        child_care['Location'] = item[2]
        child_care['PhoneNum'] = item[3]
        child_care['OpenHours'] = item[4]
        child_care['Cost'] = item[5]
        child_care['ChildCareName'] = item[6]

        items.append(child_care)
    conn.close()
    print(items)

    if request.method == 'POST':
        location = request.form['location']
        phone_num = request.form['phone_num']
        open_hours = request.form['open_hours']
        cost = request.form['cost']
        childcare_name = request.form['childcare_name']

        if location == '' or phoneNum == '' or open_hours == '' or cost == '' or childcare_name == '':
            msg = 'Make sure you filled our all the fields completely when uploading an item!'
        else:
            ts = time.time()
            timestamp = datetime.datetime.\
                fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

            conn = MySQLdb.connect(host=DB_HOSTNAME,
                                   user=DB_USERNAME,
                                   passwd=DB_PASSWORD,
                                   db=DB_NAME,
                                   port=3306)
            cursor = conn.cursor()

            statement = f"INSERT INTO {DB_NAME}.ChildCareData (creation_time, location, phone_num, open_hours, cost, childcare_name) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phone_num+"', '" +\
                        open_hours+"', '" +\
                        cost+"', '" +\
                        childcare_name+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/childcare')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/communityItems/childcare.html', inSession=inSession, childcare=items, msg=msg)


@app.route('/events', methods=['GET', 'POST'])
def events():
    msg = ''
    inSession = None
    if 'loggedin' in session:
        inSession = session['username']
    else:
        msg = 'You can only view these options.'

    conn = MySQLdb.connect(host=DB_HOSTNAME,
                           user=DB_USERNAME,
                           passwd=DB_PASSWORD,
                           db=DB_NAME,
                           port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM DB_NAME.EventsData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        event = {}
        event['EventID'] = item[0]
        event['CreationTime'] = item[1]
        event['Location'] = item[2]
        event['PhoneNum'] = item[3]
        event['DateTime'] = item[4]
        event['EntranceFee'] = item[5]
        event['EventName'] = item[6]

        items.append(event)
    conn.close()
    print(items)

    if request.method == 'POST':
        location = request.form['location']
        phone_num = request.form['phone_num']
        date_time = request.form['date_time']
        entrance_fee = request.form['entrance_fee']
        event_name = request.form['event_name']

        if location == '' or phoneNum == '' or date_time == '' or entrance_fee == '' or event_name == '':
            msg = 'Make sure you filled our all the fields completely when uploading an item!'
        else:
            ts = time.time()
            timestamp = datetime.datetime.\
                fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

            conn = MySQLdb.connect(host=DB_HOSTNAME,
                                   user=DB_USERNAME,
                                   passwd=DB_PASSWORD,
                                   db=DB_NAME,
                                   port=3306)
            cursor = conn.cursor()

            statement = f"INSERT INTO {DB_NAME}.EventsData (creation_time, location, phone_num, date_time, entrance_fee, event_name) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phone_num+"', '" +\
                        date_time+"', '" +\
                        entrance_fee+"', '" +\
                        event_name+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/events')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/communityItems/events.html', inSession=inSession, events=items, msg=msg)


@app.route('/groups', methods=['GET', 'POST'])
def groups():
    msg = ''
    inSession = None
    if 'loggedin' in session:
        inSession = session['username']
    else:
        msg = 'You can only view these options.'

    conn = MySQLdb.connect(host=DB_HOSTNAME,
                           user=DB_USERNAME,
                           passwd=DB_PASSWORD,
                           db=DB_NAME,
                           port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM DB_NAME.GroupsData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        group = {}
        group['GroupID'] = item[0]
        group['CreationTime'] = item[1]
        group['Location'] = item[2]
        group['PhoneNum'] = item[3]
        group['SessionHours'] = item[4]
        group['Cost'] = item[5]
        group['GroupName'] = item[6]

        items.append(group)
    conn.close()
    print(items)

    if request.method == 'POST':
        location = request.form['location']
        phone_num = request.form['phone_num']
        session_hours = request.form['session_hours']
        cost = request.form['cost']
        group_name = request.form['group_name']

        if location == '' or phoneNum == '' or session_hours == '' or cost == '' or group_name == '':
            msg = 'Make sure you filled our all the fields completely when uploading an item!'
        else:
            ts = time.time()
            timestamp = datetime.datetime.\
                fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

            conn = MySQLdb.connect(host=DB_HOSTNAME,
                                   user=DB_USERNAME,
                                   passwd=DB_PASSWORD,
                                   db=DB_NAME,
                                   port=3306)
            cursor = conn.cursor()

            statement = f"INSERT INTO {DB_NAME}.GroupsData (creation_time, location, phone_num, session_hours, cost, group_name) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phone_num+"', '" +\
                        session_hours+"', '" +\
                        cost+"', '" +\
                        group_name+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/groups')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/communityItems/groups.html', inSession=inSession, groups=items, msg=msg)


@app.route('/musicians', methods=['GET', 'POST'])
def musicians():
    msg = ''
    inSession = None
    if 'loggedin' in session:
        inSession = session['username']
    else:
        msg = 'You can only view these options.'

    conn = MySQLdb.connect(host=DB_HOSTNAME,
                           user=DB_USERNAME,
                           passwd=DB_PASSWORD,
                           db=DB_NAME,
                           port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM DB_NAME.MusiciansData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        musician = {}
        musician['MusicianID'] = item[0]
        musician['CreationTime'] = item[1]
        musician['Location'] = item[2]
        musician['PhoneNum'] = item[3]
        musician['MusicianName'] = item[4]
        musician['Genre'] = item[5]

        items.append(musician)
    conn.close()
    print(items)

    if request.method == 'POST':
        location = request.form['location']
        phone_num = request.form['phone_num']
        musician_name = request.form['musician_name']
        genre = request.form['genre']

        if location == '' or phoneNum == '' or musician_name == '' or genre == '':
            msg = 'Make sure you filled our all the fields completely when uploading an item!'
        else:
            ts = time.time()
            timestamp = datetime.datetime.\
                fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

            conn = MySQLdb.connect(host=DB_HOSTNAME,
                                   user=DB_USERNAME,
                                   passwd=DB_PASSWORD,
                                   db=DB_NAME,
                                   port=3306)
            cursor = conn.cursor()

            statement = f"INSERT INTO {DB_NAME}.MusiciansData (creation_time, location, phone_num, musician_name, genre) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phone_num+"', '" +\
                        musician_name+"', '" +\
                        genre+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/musicians')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/communityItems/musicians.html', inSession=inSession, musicians=items, msg=msg)


if __name__ == "__main__":
    app.debug = True
    app.run()
