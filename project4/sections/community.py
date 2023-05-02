from flask import request, session
from flask import render_template, redirect
from app import app
import time
import datetime
import MySQLdb
import MySQLdb.cursors

from sections.config import DB_HOSTNAME, DB_USERNAME, DB_PASSWORD, DB_NAME

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
    cursor.execute(f"SELECT * FROM {DB_NAME}.ActivitiesData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        activities = {}
        activities['ActivityID'] = item[0]
        activities['CreationTime'] = item[1]
        activities['Location'] = item[2]
        activities['PhoneNum'] = item[3]
        activities['AgeGroup'] = item[4]
        activities['TimeDate'] = item[5]
        activities['Title'] = item[6]
        activities['Capacity'] = item[7]
        items.append(activities)
    conn.close()
    print(items)

    if request.method == 'POST':
        location = request.form['location']
        phone_num = request.form['phone_num']
        age_group = request.form['age_group']
        time_date = request.form['time_date']
        title = request.form['title']
        capacity = request.form['capacity']

        if location == '' or phone_num == '' or age_group == '' or time_date == '' or title == '' or capacity == '':
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

            statement = f"INSERT INTO {DB_NAME}.ActivitiesData (creation_time, location, phone_num, age_group, time_date, title, capacity) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phone_num+"', '" +\
                        age_group+"', '" +\
                        time_date+"', '" +\
                        title+"', '" +\
                        capacity+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/activities')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/communityItems/activities.html', inSession=inSession, activities=items, msg=msg)

@app.route('/performers', methods=['GET', 'POST'])
def performers():
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
    cursor.execute(f"SELECT * FROM {DB_NAME}.PerformersData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        performers = {}
        performers['PerformerID'] = item[0]
        performers['CreationTime'] = item[1]
        performers['Location'] = item[2]
        performers['PhoneNum'] = item[3]
        performers['PerformerName'] = item[4]
        performers['Genre'] = item[5]
        performers['ShowTime'] = item[6]
        performers['AgeRating'] = item[7]
        items.append(performers)
    conn.close()
    print(items)

    if request.method == 'POST':
        location = request.form['location']
        phone_num = request.form['phone_num']
        performer_name = request.form['performer_name']
        genre = request.form['genre']
        show_time = request.form['show_time']
        age_rating = request.form['age_rating']

        if location == '' or phone_num == '' or performer_name == '' or genre == '' or show_time == '' or age_rating == '':
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

            statement = f"INSERT INTO {DB_NAME}.PerformersData (creation_time, location, phone_num, performer_name, genre, show_time, age_rating) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phone_num+"', '" +\
                        performer_name+"', '" +\
                        genre+"', '" +\
                        show_time+"', '" +\
                        age_rating+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/performers')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/communityItems/performers.html', inSession=inSession, performers=items, msg=msg)

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
    cursor.execute(f"SELECT * FROM {DB_NAME}.ChildCareData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        childcare = {}
        childcare['ChildCareID'] = item[0]
        childcare['CreationTime'] = item[1]
        childcare['Location'] = item[2]
        childcare['PhoneNum'] = item[3]
        childcare['OpenHours'] = item[4]
        childcare['Cost'] = item[5]
        childcare['ChildCareName'] = item[6]
        childcare['Capacity'] = item[7]
        items.append(childcare)
    conn.close()
    print(items)

    if request.method == 'POST':
        location = request.form['location']
        phone_num = request.form['phone_num']
        open_hours = request.form['open_hours']
        cost = request.form['cost']
        childcare_name = request.form['childcare_name']
        capacity = request.form['capacity']

        if location == '' or phone_num == '' or open_hours == '' or cost == '' or childcare_name == '' or capacity == '':
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

            statement = f"INSERT INTO {DB_NAME}.ChildCareData (creation_time, location, phone_num, open_hours, cost, childcare_name, capacity) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phone_num+"', '" +\
                        open_hours+"', '" +\
                        cost+"', '" +\
                        childcare_name+"', '" +\
                        capacity+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/childcare')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/communityItems/childcare.html', inSession=inSession, childcare=items, msg=msg)


@app.route('/rideshare', methods=['GET', 'POST'])
def rideshare():
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
    cursor.execute(f"SELECT * FROM {DB_NAME}.RideshareData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        rideshare = {}
        rideshare['RideshareID'] = item[0]
        rideshare['CreationTime'] = item[1]
        rideshare['PickupLocation'] = item[2]
        rideshare['PhoneNum'] = item[3]
        rideshare['DateTime'] = item[4]
        rideshare['DropoffLocation'] = item[5]
        rideshare['Pay'] = item[6]
        rideshare['People'] = item[7]
        items.append(rideshare)
    conn.close()
    print(items)

    if request.method == 'POST':
        pickup_location = request.form['pickup_location']
        phone_num = request.form['phone_num']
        date_time = request.form['date_time']
        dropoff_location = request.form['dropoff_location']
        pay = request.form['pay']
        people = request.form['people']

        if pickup_location == '' or phone_num == '' or date_time == '' or dropoff_location == '' or pay == '' or people == '':
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

            statement = f"INSERT INTO {DB_NAME}.RideshareData (creation_time, pickup_location, phone_num, date_time, dropoff_location, pay, people) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        pickup_location+"', '" +\
                        phone_num+"', '" +\
                        date_time+"', '" +\
                        dropoff_location+"', '" +\
                        pay+"', '" +\
                        people+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/rideshare')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/communityItems/rideshare.html', inSession=inSession, rideshare=items, msg=msg)


@app.route('/clubs', methods=['GET', 'POST'])
def clubs():
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
    cursor.execute(f"SELECT * FROM {DB_NAME}.ClubsData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        clubs = {}
        clubs['ClubID'] = item[0]
        clubs['CreationTime'] = item[1]
        clubs['Location'] = item[2]
        clubs['PhoneNum'] = item[3]
        clubs['SessionHours'] = item[4]
        clubs['Cost'] = item[5]
        clubs['ClubName'] = item[6]
        clubs['Capacity'] = item[7]
        items.append(clubs)
    conn.close()
    print(items)

    if request.method == 'POST':
        location = request.form['location']
        phone_num = request.form['phone_num']
        session_hours = request.form['session_hours']
        cost = request.form['cost']
        club_name = request.form['club_name']
        capacity = request.form['capacity']

        if location == '' or phone_num == '' or session_hours == '' or cost == '' or club_name == '' or capacity == '':
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

            statement = f"INSERT INTO {DB_NAME}.ClubsData (creation_time, location, phone_num, session_hours, cost, club_name, capacity) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phone_num+"', '" +\
                        session_hours+"', '" +\
                        cost+"', '" +\
                        club_name+"', '" +\
                        capacity+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/clubs')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/communityItems/clubs.html', inSession=inSession, clubs=items, msg=msg)