from flask import request, session
from flask import render_template, redirect
from app import app
import time
import datetime
import MySQLdb
import MySQLdb.cursors

from sections.config import DB_HOSTNAME, DB_USERNAME, DB_PASSWORD, DB_NAME
#healthcare, engineering, education, transportation, finance
@app.route('/healthcare', methods=['GET', 'POST'])
def healthcare():
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
    cursor.execute(f"SELECT * FROM {DB_NAME}.HealthcareData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        healthcare = {}
        healthcare['HealthcareID'] = item[0]
        healthcare['CreationTime'] = item[1]
        healthcare['Location'] = item[2]
        healthcare['Email'] = item[3]
        healthcare['Salary'] = item[4]
        healthcare['Experience'] = item[5]
        healthcare['Title'] = item[6]
        healthcare['Employer'] = item[7]
        items.append(healthcare)
    conn.close()
    print(items)

    if request.method == 'POST':
        salary = request.form['salary']
        location = request.form['location']
        email = request.form['email']
        experience = request.form['experience']
        title = request.form['title']
        employer = request.form['employer']

        if salary == '' or location == '' or email == '' or experience == '' or title == '' or employer == '':
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

            statement = f"INSERT INTO {DB_NAME}.HealthcareData (creation_time, location, email, salary, experience, title, employer) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        email+"', '" +\
                        salary+"', '" +\
                        experience+"', '" +\
                        title+"', '" +\
                        employer+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/healthcare')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/jobItems/healthcare.html', inSession=inSession, healthcare=items, msg=msg)

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
    cursor.execute(f"SELECT * FROM {DB_NAME}.EngineeringData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        engineering = {}
        engineering['EngineeringID'] = item[0]
        engineering['CreationTime'] = item[1]
        engineering['Location'] = item[2]
        engineering['Email'] = item[3]
        engineering['Salary'] = item[4]
        engineering['Experience'] = item[5]
        engineering['Title'] = item[6]
        engineering['Employer'] = item[7]
        items.append(engineering)
    conn.close()
    print(items)

    if request.method == 'POST':
        salary = request.form['salary']
        location = request.form['location']
        email = request.form['email']
        experience = request.form['experience']
        title = request.form['title']
        employer = request.form['employer']

        if salary == '' or location == '' or email == '' or experience == '' or title == '' or employer == '':
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

            statement = f"INSERT INTO {DB_NAME}.EngineeringData (creation_time, location, email, salary, experience, title, employer) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        email+"', '" +\
                        salary+"', '" +\
                        experience+"', '" +\
                        title+"', '" +\
                        employer+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/engineering')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/jobItems/engineering.html', inSession=inSession, engineering=items, msg=msg)

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
    cursor.execute(f"SELECT * FROM {DB_NAME}.EducationData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        education = {}
        education['EducationID'] = item[0]
        education['CreationTime'] = item[1]
        education['Location'] = item[2]
        education['Email'] = item[3]
        education['Salary'] = item[4]
        education['Experience'] = item[5]
        education['Title'] = item[6]
        education['Employer'] = item[7]
        items.append(education)
    conn.close()
    print(items)

    if request.method == 'POST':
        salary = request.form['salary']
        location = request.form['location']
        email = request.form['email']
        experience = request.form['experience']
        title = request.form['title']
        employer = request.form['employer']

        if salary == '' or location == '' or email == '' or experience == '' or title == '' or employer == '':
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

            statement = f"INSERT INTO {DB_NAME}.EducationData (creation_time, location, email, salary, experience, title, employer) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        email+"', '" +\
                        salary+"', '" +\
                        experience+"', '" +\
                        title+"', '" +\
                        employer+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/education')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/jobItems/education.html', inSession=inSession, education=items, msg=msg)

@app.route('/transportation', methods=['GET', 'POST'])
def transportation():
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
    cursor.execute(f"SELECT * FROM {DB_NAME}.TransportationData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        transportation = {}
        transportation['TransportationID'] = item[0]
        transportation['CreationTime'] = item[1]
        transportation['Location'] = item[2]
        transportation['Email'] = item[3]
        transportation['Salary'] = item[4]
        transportation['Experience'] = item[5]
        transportation['Title'] = item[6]
        transportation['Employer'] = item[7]
        items.append(transportation)
    conn.close()
    print(items)

    if request.method == 'POST':
        salary = request.form['salary']
        location = request.form['location']
        email = request.form['email']
        experience = request.form['experience']
        title = request.form['title']
        employer = request.form['employer']

        if salary == '' or location == '' or email == '' or experience == '' or title == '' or employer == '':
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

            statement = f"INSERT INTO {DB_NAME}.TransportationData (creation_time, location, email, salary, experience, title, employer) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        email+"', '" +\
                        salary+"', '" +\
                        experience+"', '" +\
                        title+"', '" +\
                        employer+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/transportation')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/jobItems/transportation.html', inSession=inSession, transportation=items, msg=msg)


@app.route('/finance', methods=['GET', 'POST'])
def finance():
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
    cursor.execute(f"SELECT * FROM {DB_NAME}.FinanceData;")
    results = cursor.fetchall()

    items = []
    for item in results:
        finance = {}
        finance['FinanceID'] = item[0]
        finance['CreationTime'] = item[1]
        finance['Location'] = item[2]
        finance['Email'] = item[3]
        finance['Salary'] = item[4]
        finance['Experience'] = item[5]
        finance['Title'] = item[6]
        finance['Employer'] = item[7]
        items.append(finance)
    conn.close()
    print(items)

    if request.method == 'POST':
        salary = request.form['salary']
        location = request.form['location']
        email = request.form['email']
        experience = request.form['experience']
        title = request.form['title']
        employer = request.form['employer']

        if salary == '' or location == '' or email == '' or experience == '' or title == '' or employer == '':
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

            statement = f"INSERT INTO {DB_NAME}.FinanceData (creation_time, location, email, salary, experience, title, employer) VALUES (" +\
                        "'"+str(timestamp)+"', '" +\
                        location+"', '" +\
                        email+"', '" +\
                        salary+"', '" +\
                        experience+"', '" +\
                        title+"', '" +\
                        employer+"');"

            print(statement)
            result = cursor.execute(statement)
            conn.commit()
            conn.close()

            return redirect('/finance')
    else:
        msg = 'Sign up or Login if you want to upload items!'

    return render_template('/jobItems/finance.html', inSession=inSession, finance=items, msg=msg)