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
        activity = {}
        activity['ActivityID'] = item[0]
        activity['CreationTime'] = item[1]
        activity['Location'] = item[2]
        activity['PhoneNum'] = item[3]
        activity['AgeGroup'] = item[4]
        activity['TimeDate'] = item[5]
        activity['Title'] = item[6]
        activity['Capacity'] = item[7]

        items.append(activity)
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
        performer = {}
        performer['PerformerID'] = item[0]
        performer['CreationTime'] = item[1]
        performer['Location'] = item[2]
        performer['PhoneNum'] = item[3]
        performer['PerformerName'] = item[4]
        performer['Genre'] = item[5]
        performer['ShowTime'] = item[6]
        performer['AgeRating'] = item[7]

        items.append(performer)
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
        child_care = {}
        child_care['ChildCareID'] = item[0]
        child_care['CreationTime'] = item[1]
        child_care['Location'] = item[2]
        child_care['PhoneNum'] = item[3]
        child_care['OpenHours'] = item[4]
        child_care['Cost'] = item[5]
        child_care['ChildCareName'] = item[6]
        child_care['Capacity'] = item[7]

        items.append(child_care)
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


@app.route('/festivals', methods=['GET', 'POST'])
def festivals():
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
    cursor.execute(f"SELECT * FROM {DB_NAME}.FestivalsData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        festival = {}
        festival['FestivalID'] = item[0]
        festival['CreationTime'] = item[1]
        festival['Location'] = item[2]
        festival['PhoneNum'] = item[3]
        festival['DateTime'] = item[4]
        festival['EntranceFee'] = item[5]
        festival['FestivalName'] = item[6]
        festival['Capacity'] = item[7]

        items.append(festival)
    conn.close()
    print(items)

    if request.method == 'POST':
        location = request.form['location']
        phone_num = request.form['phone_num']
        date_time = request.form['date_time']
        entrance_fee = request.form['entrance_fee']
        festival_name = request.form['festival_name']
        capacity = request.form['capacity']

        if location == '' or phone_num == '' or date_time == '' or entrance_fee == '' or festival_name == '' or capacity == '':
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

            statement = f"INSERT INTO {DB_NAME}.FestivalsData (creation_time, location, phone_num, date_time, entrance_fee, festival_name, capacity) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        phone_num+"', '" +\
                        date_time+"', '" +\
                        entrance_fee+"', '" +\
                        festival_name+"', '" +\
                        capacity+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/festivals')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/communityItems/festivals.html', inSession=inSession, festivals=items, msg=msg)


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
        club = {}
        club['ClubID'] = item[0]
        club['CreationTime'] = item[1]
        club['Location'] = item[2]
        club['PhoneNum'] = item[3]
        club['SessionHours'] = item[4]
        club['Cost'] = item[5]
        club['ClubName'] = item[6]
        club['Capacity'] = item[7]

        items.append(club)
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