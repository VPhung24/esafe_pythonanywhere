# A very simple Flask Hello World app for you to get started with...
import sys
from flask import Flask, render_template, flash, request, url_for, redirect, session
from flask import *
from functools import wraps
import MySQLdb
import MySQLdb.cursors
import os
from twilio.rest import Client
from requests import Request, Session
from twilio.http.response import Response

# Initialize Flask app with the template folder address
app = Flask(__name__, template_folder='templates')
app.config["DEBUG"] = True

def connect_to_database():
  options = {
    'host': 'vphung.mysql.pythonanywhere-services.com',
    'user': 'vphung',
    'password': 'taylorswiftvivian',
    'db': 'vphung$esafe',
    'cursorclass': MySQLdb.cursors.DictCursor
  }
  db = MySQLdb.connect(**options)
  db.autocommit(True)
  return db

db = connect_to_database()

@app.route('/database/')
def database_path():
    db = connect_to_database()
    cursor = db.cursor()
    cursor.execute('SELECT uid, firstname, lastname, username, city, state, streetaddress, email, password, special_needs, phonenumber, zipcode FROM users')
    results = cursor.fetchall()
    db.close()
    print_str = "<table>"
    for result in results:
        print_str += "<tr><td> %s <br></td><td> %s <br></td><td> %s <br></td><td> %s <br></td><td> %s <br></td><td> %s <br></td><td> %s <br></td><td> %s <br></td><td> %s <br></td><td> %s <br></td><td> %s <br></td><td> %s <br></td><tr>" % (result['uid'], result['firstname'], result['lastname'], result['username'], result['city'], result['state'], result['streetaddress'], result['email'], result['password'], result['special_needs'], result['phonenumber'], result['zipcode'])
    print_str += "</table>"
    print(session['logged_in'])
    if 'user' in session:
        logged_in = True
        return render_template("database.html", results = results, logged_in = logged_in, username = session['user'], admin = session['admin'])
    else:
        logged_in = False
        return render_template("database.html", results = results, logged_in = logged_in)

@app.route("/")
def main_route():
    if 'user' in session:
        logged_in = True
        return render_template('index.html', logged_in = logged_in, username = session['user'])
    else:
        logged_in = False
        return render_template('index.html', logged_in = logged_in)

app.secret_key = 'vivian and serina is cool'

@app.errorhandler(404)
def page_not_found(e):
	options = {
		"edit": False
	}
	return render_template("404.html" , **options)

@app.errorhandler(405)
def method_not_found(e):
	options = {
		"edit": False
	}
	return render_template("405.html" , **options)

@app.route('/slashboard/')
def slashboard():
	try:
		return render_template("index.html")
	except Exception as e:
		return render_template("500.html", error = e)

@app.route("/earthquakes/")
def earthquake_route():
	if 'user' in session:
		logged_in = True
		return render_template('earthquakes.html', logged_in = logged_in, username = session['user'])
	else:
		logged_in = False
		return render_template('earthquakes.html', logged_in = logged_in)

@app.route("/emergency_contact/")
def emergency_contact_route():
	if 'user' in session:
		logged_in = True
		return render_template('emergency_contact.html', logged_in = logged_in, username = session['user'])
	else:
		logged_in = False
		return render_template('emergency_contact.html', logged_in = logged_in)

@app.route("/flooding/")
def flooding_route():
	if 'user' in session:
		logged_in = True
		return render_template("flooding.html" , logged_in = logged_in, username = session['user'])
	else:
		logged_in = False
		return render_template("flooding.html" , logged_in = logged_in)

@app.route("/landslides/")
def landslides_route():
	if 'user' in session:
		logged_in = True
		return render_template('landslides.html', logged_in = logged_in, username = session['user'])
	else:
		logged_in = False
		return render_template('landslides.html', logged_in = logged_in)

@app.route('/login/', methods=["GET","POST"])
def login_page():

  # session.pop('user', None)

  if request.method == "POST":
    attempted_username = request.form['username']
    attempted_password = request.form['password']

    db = connect_to_database()
    cursor = db.cursor()
    cursor.execute('SELECT username FROM users WHERE username = %s', [attempted_username])
    test_for_username = cursor.fetchall()
    error = '' # if username exists, test that the password matches
    if not test_for_username:
      error = "Invalid credentials. Try Again."
      session['logged_in'] = False
      return render_template("login.html", error = error, logged_in = session['logged_in'])
    else:
      if not attempted_password:
        error = "Invalid credentials. Try Again."
        session['logged_in'] = False
        return render_template("login.html", error = error, logged_in = session['logged_in'])
      else:
        cursor = db.cursor()
        cursor.execute('SELECT password FROM users WHERE username = %s', [attempted_username])
        results = cursor.fetchall()
        results = results[0]['password']

        if results == attempted_password:
          session['logged_in'] = True
          session['user'] = request.form['username']

          #firstname
          cursor.execute('SELECT firstname FROM users WHERE username = %s', [attempted_username])
          firstname_dict = cursor.fetchall()
          session['firstname'] = firstname_dict[0]['firstname']

          #lastname
          cursor.execute('SELECT lastname FROM users WHERE username = %s', [attempted_username])
          lastname_dict = cursor.fetchall()
          session['lastname'] = lastname_dict[0]['lastname']

          #city
          cursor.execute('SELECT city FROM users WHERE username = %s', [attempted_username])
          city_dict = cursor.fetchall()
          session['city'] = city_dict[0]['city']

          #zipcode
          cursor.execute('SELECT zipcode FROM users WHERE username = %s', [attempted_username])
          zipcode_dict = cursor.fetchall()
          session['zipcode'] = zipcode_dict[0]['zipcode']

          #state
          cursor.execute('SELECT state FROM users WHERE username = %s', [attempted_username])
          state_dict = cursor.fetchall()
          session['state'] = state_dict[0]['state']

          #streetaddress
          cursor.execute('SELECT streetaddress FROM users WHERE username = %s', [attempted_username])
          streetaddress_dict = cursor.fetchall()
          session['streetaddress'] = streetaddress_dict[0]['streetaddress']

          #email
          cursor.execute('SELECT email FROM users WHERE username = %s', [attempted_username])
          email_dict = cursor.fetchall()
          session['email'] = email_dict[0]['email']

          #special needs
          cursor.execute('SELECT special_needs FROM users WHERE username = %s', [attempted_username])
          specialneeds_dict = cursor.fetchall()
          session['special_needs'] = specialneeds_dict[0]['special_needs']

          #phonenumber
          cursor.execute('SELECT phonenumber FROM users WHERE username = %s', [attempted_username])
          phonenumber_dict = cursor.fetchall()
          session['phonenumber'] = phonenumber_dict[0]['phonenumber']

          #admin
          cursor.execute('SELECT uid FROM users WHERE username = %s', [attempted_username])
          uid_dict = cursor.fetchall()
          uid = uid_dict[0]['uid']
          admin = False

          #test
          cursor.execute('SELECT phonenumber FROM users')
          phonen_dict = cursor.fetchall()
          print(phonen_dict)

          db.close()

          if uid < 30:
            admin = True
            session['admin'] = True
          else:
            admin = False
            session['admin'] = False
          return render_template("login.html", firstname = session['firstname'], lastname = session['lastname'], city = session['city'], username = session['user'], zipcode = session['zipcode'], state = session['state'], streetaddress = session['streetaddress'], email = session['email'], logged_in = session['logged_in'], admin = session['admin'], phonenumber =  session['phonenumber'], specialneeds = session['special_needs'])  # this is the valid password and username
        else:
          session['logged_in'] = False
          error = "Invalid credentials. Try Again."
          return render_template("login.html", error = error, logged_in = session['logged_in'])  #otherwise it is wrong
  elif 'user' in session:
    return render_template("login.html", firstname = session['firstname'], lastname = session['lastname'], city = session['city'], username = session['user'], zipcode = session['zipcode'], state = session['state'], streetaddress = session['streetaddress'], email = session['email'], logged_in = session['logged_in'], admin = session['admin'], phonenumber =  session['phonenumber'], specialneeds = session['special_needs'])
  else:
    session['logged_in'] = False
    return render_template("login.html")

@app.route("/logout/", methods=["GET","POST"])
def logout_page():
	session['logged_in'] = False
	session.pop('user', None)
	session.pop('firstname', None)
	session.pop('lastname', None)
	session.pop('city', None)
	session.pop('zipcode', None)
	session.pop('state', None)
	session.pop('streetaddress', None)
	session.pop('email', None)
	return redirect("http://vphung.pythonanywhere.com/login/")

@app.route("/preparation/")
def preparation_route():
	if 'user' in session:
		logged_in = True
		return render_template('preparation.html', logged_in = logged_in, username = session['user'])
	else:
		logged_in = False
		return render_template('preparation.html', logged_in = logged_in)

@app.route('/register/', methods=["GET","POST"])
def register_page():
	error = []
	error1 = ""
	error2 = ""
	error3 = ""
	error4 = ""
	error5 = ""
	error6 = ""
	error7 = ""
	error8 = ""
	error9 = ""
	error10 = ""
	error11 = ""

	if request.method == "POST":

		# Firstname
		my_firstname = request.form['firstname']
		if (len(my_firstname) < 2):
			error1 = "Your firstname is too short. "
			error.append("firstname")
		#Lastname
		my_lastname = request.form['lastname']
		if (len(my_lastname) < 2):
			error2 = "Your lastname is too short. "
			error.append("lastname")

		#username
		my_username = request.form['username']
		if (len(my_username) < 1):
			error3 = "Your username is too short. "
			error.append("username")

		#password
		my_password = request.form['password']
		if (len(my_password) < 1):
			error4 = "Your password is too short. "
			error.append("password")

		#email
		my_email = request.form['email']
		if (len(my_email) < 5):
			error5 = "Your email must be longer then five charaters. "
			error.append("email")

		#streetaddress
		my_streetaddress = request.form['streetaddress']
		if (len(my_streetaddress) < 5):
			error6 = "Your streetaddress must be longer then five charaters. "
			error.append("streetaddress")

		#city
		my_city = request.form['city']
		if (len(my_city) < 5):
			error7 = "Your city must be longer then five charaters. "
			error.append("city")

		#zipcode
		my_zipcode = request.form['zipcode']
		if (len(my_zipcode) < 5):
			error8 = "Your zipcode must be longer then five characters. "
			error.append("zipcode")

		#state
		my_state = request.form['state']
		if (len(my_state) > 2 and len(my_state) < 2):
			error9 = "Your state Postal Code (ex. CA)"
			error.append("state")

		#phonenumber
		my_phonenumber = request.form['phonenumber']
		if (len(my_phonenumber) < 5):
			error10 = "Your phonenumber must be longer then five characters. "
			error.append("phonenumber")

		#specialneeds
		my_specialneeds = request.form['specialneeds']
		if (len(my_specialneeds) < 2):
			error11 = "Your special needs must be longer then two characters. "
			error.append("specialneeds")

		if (len(error) == 0):
		    db = connect_to_database()
		    cursor = db.cursor()
		    cursor.execute('INSERT into users(firstname, lastname, username, city, state, streetaddress, email, password, special_needs, phonenumber, zipcode) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (my_firstname, my_lastname, my_username, my_city, my_state, my_streetaddress, my_email, my_password, my_specialneeds, my_phonenumber, my_zipcode))
		    db.commit()
		    return redirect("http://vphung.pythonanywhere.com/login/")
	if 'user' in session:
		logged_in = True
		return render_template("register.html", logged_in = logged_in, username = session['user'])
	else:
		logged_in = False
		return render_template("register.html", logged_in = logged_in, errors = error, error1 = error1, error2 = error2, error3 = error3, error4 = error4, error5 = error5, error6 = error6, error7 = error7, error8 = error8, error9 = error9, error10 = error10, error11 = error11)

@app.route("/why/")
def why_route():
	if 'user' in session:
		logged_in = True
		return render_template('why.html', logged_in = logged_in, username = session['user'])
	else:
		logged_in = False
		return render_template('why.html', logged_in = logged_in)

@app.route("/wildfires/")
def wildfires_route():
	if 'user' in session:
		logged_in = True
		return render_template('wildfires.html', logged_in = logged_in, username = session['user'])
	else:
		logged_in = False
		return render_template('wildfires.html', logged_in = logged_in)

account_sid = "ACac57689c5547072a1d467d0aa09e496b"
auth_token = "d6e71203ae75a31029fa373ceaab7fd0"

client = Client(account_sid, auth_token)
@app.route('/text/', methods=["GET","POST"])
def text_page():
	if 'user' in session:
		if request.method == "POST":
		    db = connect_to_database()
		    cursor = db.cursor()
		    cursor.execute('SELECT phonenumber FROM users')
		    phonen_dict = cursor.fetchall()
		    db.close()
		    my_test_prompt = request.form['text']
		    for numbers in phonen_dict:
		    	client.messages.create(
		    		to = numbers['phonenumber'],
					from_= "+15104221809",
					body= my_test_prompt
				)
			logged_in = True
			return render_template('text.html', logged_in = logged_in, username = session['user'], admin = session['admin'])
		else:
			logged_in = True
			return render_template('text.html', logged_in = logged_in, username = session['user'], admin = session['admin'])
	else:
		logged_in = False
		return render_template('text.html', logged_in = logged_in)

# if __name__ == '__main__':
#     # listen on external IPs
#     app.run(host=config.env['host'], port=config.env['port'], debug=True)