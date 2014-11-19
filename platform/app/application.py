
# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, make_response, current_app, jsonify
from contextlib import closing
import json
from datetime import timedelta
from functools import update_wrapper
import MySQLdb

# from flask.ext.sqlalchemy import SQLAlchemy

# from database import db_session
# from database import init_db
# from models import User

from sqlalchemy import create_engine, MetaData, Table
import time

# configuration
# DATABASE = '/home/ec2-user/mechakaijuwars/platform/app/tmp/platform.db'
# DEBUG = True
# SECRET_KEY = 'development key'
# USERNAME = 'admin'
# PASSWORD = 'default'

# create our little application :)
application = Flask(__name__)
application.config.from_object(__name__)
application.config.from_envvar('PLATFORM_SETTINGS', silent=True)

engine = create_engine('mysql://space_noodel:tack3toM@mkw.c488gn8kr4wp.us-west-2.rds.amazonaws.com:3306/mkw', convert_unicode=True)
metadata = MetaData(bind=engine)

users = Table('users', metadata, autoload=True)

@application.before_request
def before_request():
    t = time.time()
    con = engine.connect()
    con.execute(users.insert(), name='admin' + str(t), email='admin@localhost' + str(t))
	
# @application.teardown_appcontext
# def shutdown_session(exception=None):
# 	db_session.remove()

@application.teardown_request
def teardown_request(exception):
    print 'teardown'
def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

# @app.route('/login', methods=['GET', 'POST'])
# def login():
# 	error = None
# 	if request.method == 'POST':
# 		if request.form['username'] != app.config['USERNAME']:
# 			error = 'Invalid username'
# 		elif request.form['password'] != app.config['PASSWORD']:
# 			error = 'Invalid password'
# 		else:
# 			session['logged_in'] = True
# 			flash('You were logged in')
# 			return redirect(url_for('show_entries'))
# 	return render_template('login.html', error=error)

# @app.route('/logout')
# def logout():
# 	session.pop('logged_in', None)
# 	flash('You were logged out')
# 	return redirect(url_for('show_entries'))

@application.route('/my_service', methods=['GET', 'POST'])
@crossdomain(origin='*')
def my_service():
    # message = request.get_json().get('name', '')
    # print str(request.data)
    # print request.args.get('p')
    return json.dumps({'init':{'host':'prod-platform', 'response': str(users.select(users.c.id == 1).execute().first())}})

if __name__ == '__main__':
    application.run('0.0.0.0')
