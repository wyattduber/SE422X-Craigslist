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

@app.route('/golfCarts', methods=['GET', 'POST'])
def golfCarts():
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
    cursor.execute(f"SELECT * FROM {DB_NAME}.GolfCartData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        golfCart = {}
        golfCart['GolfCartID'] = item[0]
        golfCart['CreationTime'] = item[1]
        golfCart['Price'] = item[2]
        golfCart['Location'] = item[3]
        golfCart['PhoneNum'] = item[4]
        golfCart['CurrCondition'] = item[5]
        golfCart['MakeModel'] = item[6]
        golfCart['YearBuilt'] = item[7]
        golfCart['Color'] = item[8]
        golfCart['FuelType'] = item[9]
        items.append(golfCart)
    conn.close()
    print(items)

    if request.method == 'POST':
        price = request.form['price']
        location = request.form['location']
        phoneNum = request.form['phoneNum']
        condition = request.form['condition']
        make_model = request.form['make_model']
        year_built = request.form['year_built']
        color = request.form['color']
        fuel_type = request.form['fuel_type']

        if price == '' or location == '' or phoneNum == '' or condition == '' or make_model == '' or year_built == '' or color == '' or fuel_type == '':
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

            statement = f"INSERT INTO {DB_NAME}.GolfCartData (creation_time, price, location, phoneNum, curr_condition, make_model, year_built, color, fuel_type) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        price+"', '" +\
                        location+"', '" +\
                        phoneNum+"', '" +\
                        condition+"', '" +\
                        make_model+"', '" +\
                        year_built+"', '" +\
                        color+"', '" +\
                        fuel_type+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()
            return redirect('/golfCarts')
    else:
        msg = 'You can only view these options. Sign up or Login if you want to upload items!'

    return render_template('/forSale/golfCarts.html', inSession=inSession, golfCarts=items, msg=msg)

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
    cursor.execute(f"SELECT * FROM {DB_NAME}.BikeData;")
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

    return render_template('/forSale/bikes.html', inSession=inSession, bikes=items, msg=msg)

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
    cursor.execute(f"SELECT * FROM {DB_NAME}.BoatData;")
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

    return render_template('/forSale/boats.html', inSession=inSession, boats=items, msg=msg)


@app.route('/cell-phones', methods=['GET', 'POST'])
def cellPhones():
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
    cursor.execute(f"SELECT * FROM {DB_NAME}.CellPhoneData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        cellphone = {}
        cellphone['CellPhoneID'] = item[0]
        cellphone['CreationTime'] = item[1]
        cellphone['Price'] = item[2]
        cellphone['Location'] = item[3]
        cellphone['PhoneNum'] = item[4]
        cellphone['Manufacturer'] = item[5]
        cellphone['Model'] = item[6]
        cellphone['Memory'] = item[7]
        items.append(cellphone)
    conn.close()
    print(items)

    if request.method == 'POST':
        price = request.form['price']
        location = request.form['location']
        phoneNum = request.form['phoneNum']
        manufacturer = request.form['manufacturer']
        model = request.form['model']
        memory = request.form['memory']

        if price == '' or location == '' or phoneNum == '' or manufacturer == '' or model == '' or memory == '':
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

            statement = f"INSERT INTO {DB_NAME}.CellPhoneData (creation_time, price, location, phoneNum, manufacturer, model, memory) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        price+"', '" +\
                        location+"', '" +\
                        phoneNum+"', '" +\
                        manufacturer+"', '" +\
                        model+"', '" +\
                        memory+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/cell-phones')
    else:
        msg = 'You can only view these options. Sign up or Login if you want to upload items!'
    return render_template('/forSale/cellphones.html', inSession=inSession, cellPhones=items, msg=msg)


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
    cursor.execute(f"SELECT * FROM {DB_NAME}.FurnitureData;")
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
