from flask import *
from extensions import *
from functools import *

register = Blueprint('register', __name__, template_folder='templates')
				
@register.route('/register/', methods=["GET","POST"])
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
			cursor = db.cursor()
			print(error)
			cursor.execute('INSERT into users(firstname, lastname, username, city, state, streetaddress, email, password, special_needs, phonenumber, zipcode) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (my_firstname, my_lastname, my_username, my_city, my_state, my_streetaddress, my_email, my_password, my_specialneeds, my_phonenumber, my_zipcode)) 
			return redirect("http://localhost:1989/login/")
	if 'user' in session:
		logged_in = True
		return render_template("register.html", logged_in = logged_in, username = session['user'])
	else:
		logged_in = False
		return render_template("register.html", logged_in = logged_in, errors = error, error1 = error1, error2 = error2, error3 = error3, error4 = error4, error5 = error5, error6 = error6, error7 = error7, error8 = error8, error9 = error9, error10 = error10, error11 = error11)
