import functions as db
from flask import Flask, jsonify, request, make_response, url_for, session, Blueprint
from flask import render_template, redirect
from app import app
import os
import time
import datetime
import MySQLdb
import MySQLdb.cursors
import re

from sections.config import DB_HOSTNAME, DB_USERNAME, DB_PASSWORD, DB_NAME

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
    cursor.execute(f"SELECT * FROM {DB_NAME}.ApartmentData;")
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
        apartment['Pets'] = item[8]
        apartment['Laundry'] = item[9]
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
        pets = request.form['pets']
        laundry = request.form['laundry']

        if rent == '' or location == '' or phoneNum == '' or square_feet == '' or num_bathrooms == '' or num_bedrooms == '' or pets == '' or laundry == '':
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

            statement = f"INSERT INTO {DB_NAME}.ApartmentData (creation_time, location, phone_num, rent, square_feet, num_bathrooms, num_bedrooms, pets, laundry) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phoneNum+"', '" +\
                        rent+"', '" +\
                        square_feet+"', '" +\
                        num_bathrooms+"', '" +\
                        num_bedrooms+"', '" +\
                        pets+"', '" +\
                        laundry+"');"

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
    cursor.execute(f"SELECT * FROM {DB_NAME}.OfficesData;")
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
    cursor.execute(f"SELECT * FROM {DB_NAME}.RoomsData;")
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
        room['Term'] = item[6]
        room['Furnished'] = item[7]
        room['Gender'] = item[8]
        items.append(room)
    conn.close()
    print(items)

    if request.method == 'POST':
        rent = request.form['rent']
        location = request.form['location']
        phoneNum = request.form['phoneNum']
        square_feet = request.form['square_feet']
        term = request.form['term']
        furnished = request.form['furnished']
        gender = request.form['gender']

        if rent == '' or location == '' or phoneNum == '' or square_feet == '' or term == '' or furnished == '' or gender == '':
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

            statement = f"INSERT INTO {DB_NAME}.RoomsData (creation_time, location, phone_num, rent, square_feet, term, furnished, gender) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phoneNum+"', '" +\
                        rent+"', '" +\
                        square_feet+"', '" +\
                        term+"', '" +\
                        furnished+"', '" +\
                        gender+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()
            return redirect('/rooms')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/housingItems/rooms.html', inSession=inSession, rooms=items, msg=msg)

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
    cursor.execute(f"SELECT * FROM {DB_NAME}.RealEstateData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        realEstate = {}
        realEstate['RealEstateID'] = item[0]
        realEstate['CreationTime'] = item[1]
        realEstate['Location'] = item[2]
        realEstate['PhoneNum'] = item[3]
        realEstate['Cost'] = item[4]
        realEstate['Acreage'] = item[5]
        realEstate['Type'] = item[6]
        realEstate['Rooms'] = item[7]
        items.append(realEstate)
    conn.close()
    print(items)

    if request.method == 'POST':
        cost = request.form['cost']
        location = request.form['location']
        phoneNum = request.form['phoneNum']
        acreage = request.form['acreage']
        type = request.form['type']
        rooms = request.form['rooms']

        if cost == '' or location == '' or phoneNum == '' or acreage == '' or type == '' or rooms == '':
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

            statement = f"INSERT INTO {DB_NAME}.RealEstateData (creation_time, location, phone_num, cost, acreage, type, rooms) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phoneNum+"', '" +\
                        cost+"', '" +\
                        acreage+"', '" +\
                        type+"', '" +\
                        rooms+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/realEstate')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/housingItems/realEstate.html', inSession=inSession, realEstates=items, msg=msg)

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
    cursor.execute(f"SELECT * FROM {DB_NAME}.VacationData;")
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
        vacation['Pool'] = item[6]
        vacation['Firepit'] = item[7]
        items.append(vacation)
    conn.close()
    print(items)

    if request.method == 'POST':
        location = request.form['location']
        phoneNum = request.form['phoneNum']
        cost_per_night = request.form['cost_per_night']
        num_beds = request.form['num_beds']
        pool = request.form['pool']
        firepit = request.form['firepit']

        if cost_per_night == '' or location == '' or phoneNum == '' or num_beds == '' or pool == '' or firepit == '':
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

            statement = f"INSERT INTO {DB_NAME}.VacationData (creation_time, location, phone_num, cost_per_night, num_beds, pool, firepit) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phoneNum+"', '" +\
                        cost_per_night+"', '" +\
                        num_beds+"', '" +\
                        pool+"', '" +\
                        firepit+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/vacation')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/housingItems/vacation.html', inSession=inSession, vacations=items, msg=msg)