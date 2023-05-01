from flask import request, session
from flask import render_template, redirect
from app import app
import time
import datetime
import MySQLdb
import MySQLdb.cursors

from sections.config import DB_HOSTNAME, DB_USERNAME, DB_PASSWORD, DB_NAME

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

            statement = "INSERT INTO DB_NAME.AccountingData (creation_time, location, phone_num, salary, experience, remote_person, title, company_name) VALUES (" +\
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

            statement = "INSERT INTO DB_NAME.EngineeringData (creation_time, location, phone_num, salary, experience, remote_person, title, company_name) VALUES (" +\
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

            statement = "INSERT INTO DB_NAME.EducationData (creation_time, location, phone_num, salary, experience, remote_person, title, company_name) VALUES (" +\
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

            statement = "INSERT INTO DB_NAME.LaborData (creation_time, location, phone_num, salary, experience, remote_person, title, company_name) VALUES (" +\
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

            statement = "INSERT INTO DB_NAME.RetailData (creation_time, location, phone_num, salary, experience, remote_person, title, company_name) VALUES (" +\
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