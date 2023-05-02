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

@app.route('/lawn', methods=['GET', 'POST'])
def lawnCare():
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
    cursor.execute(f"SELECT * FROM {DB_NAME}.LawnData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        lawn = {}
        lawn['LawnID'] = item[0]
        lawn['CreationTime'] = item[1]
        lawn['Location'] = item[2]
        lawn['PhoneNum'] = item[3]
        lawn['Cost'] = item[4]
        lawn['OperatingHours'] = item[5]
        lawn['CompanyName'] = item[6]
        lawn['ServiceType'] = item[7]
        items.append(lawn)
    conn.close()
    print(items)

    if request.method == 'POST':
        cost = request.form['cost']
        location = request.form['location']
        phoneNum = request.form['phoneNum']
        operating_hours = request.form['operating_hours']
        company_name = request.form['company_name']
        service_type = request.form['service_type']

        if cost == '' or location == '' or phoneNum == '' or operating_hours == '' or company_name == '' or service_type == '':
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

            statement = f"INSERT INTO {DB_NAME}.LawnData (creation_time, location, phone_num, cost, operating_hours, company_name, service_type) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phoneNum+"', '" +\
                        cost+"', '" +\
                        operating_hours+"', '" +\
                        company_name+"', '" +\
                        service_type+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()
            return redirect('/lawn')
    else:
        msg = 'You can only view these options. Sign up or Login if you want to upload items!'

    return render_template('/serviceItems/lawn.html', inSession=inSession, lawn=items, msg=msg)


@app.route('/phone', methods=['GET', 'POST'])
def phone():
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
    cursor.execute(f"SELECT * FROM {DB_NAME}.PhoneData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        phone = {}
        phone['PhoneID'] = item[0]
        phone['CreationTime'] = item[1]
        phone['Location'] = item[2]
        phone['PhoneNum'] = item[3]
        phone['Cost'] = item[4]
        phone['OperatingHours'] = item[5]
        phone['CompanyName'] = item[6]
        phone['RepairType'] = item[7]
        items.append(phone)
    conn.close()
    print(items)

    if request.method == 'POST':
        cost = request.form['cost']
        location = request.form['location']
        phoneNum = request.form['phoneNum']
        operating_hours = request.form['operating_hours']
        company_name = request.form['company_name']
        repair_type = request.form['repair_type']

        if cost == '' or location == '' or phoneNum == '' or operating_hours == '' or company_name == '' or repair_type == '':
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

            statement = f"INSERT INTO {DB_NAME}.PhoneData (creation_time, location, phone_num, cost, operating_hours, company_name, repair_type) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phoneNum+"', '" +\
                        cost+"', '" +\
                        operating_hours+"', '" +\
                        company_name+"', '" +\
                        repair_type+"');" 

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()
            return redirect('/phone')
    else:
        msg = 'You can only view these options. Sign up or Login if you want to upload items!'

    return render_template('/serviceItems/phone.html', inSession=inSession, phone=items, msg=msg)

@app.route('/plumbing', methods=['GET', 'POST'])
def plumbing():
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
    cursor.execute(f"SELECT * FROM {DB_NAME}.PlumbingData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        plumbing = {}
        plumbing['PlumbingID'] = item[0]
        plumbing['CreationTime'] = item[1]
        plumbing['Location'] = item[2]
        plumbing['PhoneNum'] = item[3]
        plumbing['Cost'] = item[4]
        plumbing['OperatingHours'] = item[5]
        plumbing['CompanyName'] = item[6]
        plumbing['RepairType'] = item[7]
        items.append(plumbing)
    conn.close()
    print(items)

    if request.method == 'POST':
        cost = request.form['cost']
        location = request.form['location']
        phoneNum = request.form['phoneNum']
        operating_hours = request.form['operating_hours']
        company_name = request.form['company_name']
        repair_type = request.form['repair_type']

        if cost == '' or location == '' or phoneNum == '' or operating_hours == '' or company_name == '' or repair_type == '':
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

            statement = f"INSERT INTO {DB_NAME}.PlumbingData (creation_time, location, phone_num, cost, operating_hours, company_name, repair_type) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phoneNum+"', '" +\
                        cost+"', '" +\
                        operating_hours+"', '" +\
                        company_name+"', '" +\
                        repair_type+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/plumbing')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/serviceItems/plumbing.html', inSession=inSession, plumbing=items, msg=msg)

@app.route('/internet', methods=['GET', 'POST'])
def internet():
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
    cursor.execute(f"SELECT * FROM {DB_NAME}.InternetData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        internet = {}
        internet['InternetID'] = item[0]
        internet['CreationTime'] = item[1]
        internet['Location'] = item[2]
        internet['PhoneNum'] = item[3]
        internet['Cost'] = item[4]
        internet['OperatingHours'] = item[5]
        internet['CompanyName'] = item[6]
        internet['Speed'] = item[7]
        items.append(internet)
    conn.close()
    print(items)

    if request.method == 'POST':
        cost = request.form['cost']
        location = request.form['location']
        phoneNum = request.form['phoneNum']
        operating_hours = request.form['operating_hours']
        company_name = request.form['company_name']
        speed = request.form['speed']

        if cost == '' or location == '' or phoneNum == '' or operating_hours == '' or company_name == '' or speed == '':
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

            statement = f"INSERT INTO {DB_NAME}.InternetData (creation_time, location, phone_num, cost, operating_hours, company_name, speed) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phoneNum+"', '" +\
                        cost+"', '" +\
                        operating_hours+"', '" +\
                        company_name+"', '" +\
                        speed+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/internet')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/serviceItems/internet.html', inSession=inSession, internet=items, msg=msg)

@app.route('/painting', methods=['GET', 'POST'])
def painting():
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
    cursor.execute(f"SELECT * FROM {DB_NAME}.PaintingData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        paint = {}
        paint['PaintingID'] = item[0]
        paint['CreationTime'] = item[1]
        paint['Location'] = item[2]
        paint['PhoneNum'] = item[3]
        paint['Cost'] = item[4]
        paint['OperatingHours'] = item[5]
        paint['CompanyName'] = item[6]
        paint['Color'] = item[7]
        items.append(paint)
    conn.close()
    print(items)

    if request.method == 'POST':
        cost = request.form['cost']
        location = request.form['location']
        phoneNum = request.form['phoneNum']
        operating_hours = request.form['operating_hours']
        company_name = request.form['company_name']
        color = request.form['color']

        if cost == '' or location == '' or phoneNum == '' or operating_hours == '' or company_name == '' or color == '':
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

            statement = f"INSERT INTO {DB_NAME}.PaintingData (creation_time, location, phone_num, cost, operating_hours, company_name, color) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phoneNum+"', '" +\
                        cost+"', '" +\
                        operating_hours+"', '" +\
                        company_name+"', '" +\
                        color+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/painting')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/serviceItems/painting.html', inSession=inSession, paint=items, msg=msg)
