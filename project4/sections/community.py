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

        if location == '' or phone_num == '' or age_group == '' or time_date == '' or title == '':
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

            statement = "INSERT INTO DB_NAME.ActivitiesData (creation_time, location, phone_num, age_group, time_date, title) VALUES (" +\
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

        if location == '' or phone_num == '' or musician_name == '' or genre == '':
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

            statement = "INSERT INTO DB_NAME.MusiciansData (creation_time, location, phone_num, musician_name, genre) VALUES (" +\
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

        if location == '' or phone_num == '' or open_hours == '' or cost == '' or childcare_name == '':
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

            statement = "INSERT INTO DB_NAME.ChildCareData (creation_time, location, phone_num, open_hours, cost, childcare_name) VALUES (" +\
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

        if location == '' or phone_num == '' or date_time == '' or entrance_fee == '' or event_name == '':
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

            statement = "INSERT INTO DB_NAME.EventsData (creation_time, location, phone_num, date_time, entrance_fee, event_name) VALUES (" +\
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

        if location == '' or phone_num == '' or session_hours == '' or cost == '' or group_name == '':
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

            statement = "INSERT INTO DB_NAME.GroupsData (creation_time, location, phone_num, session_hours, cost, group_name) VALUES (" +\
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