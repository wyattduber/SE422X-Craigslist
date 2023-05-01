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
    cursor.execute(f"SELECT * FROM {DB_NAME}.AutomotiveData;")
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
    cursor.execute(f"SELECT * FROM {DB_NAME}.ComputerData;")
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
    cursor.execute(f"SELECT * FROM {DB_NAME}.MovingLaborData;")
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
    cursor.execute(f"SELECT * FROM {DB_NAME}.LegalData;")
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
    cursor.execute(f"SELECT * FROM {DB_NAME}.FarmData;")
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
