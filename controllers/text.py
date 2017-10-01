import os
from twilio.rest import Client
from extensions import *
from flask import *

account_sid = "ACac57689c5547072a1d467d0aa09e496b"
auth_token = "d6e71203ae75a31029fa373ceaab7fd0"

client = Client(account_sid, auth_token)

# cursor = db.cursor()
# cursor.execute('SELECT phonenumber FROM users')
# phonen_dict = cursor.fetchall()
# phonen_dict = phonen_dict
# print(phonen_dict)
# for numbers in phonen_dict:
# 	client.messages.create(
# 		to = numbers['phonenumber'], 
# 		from_= "+15104221809",
# 		body= "This is a test. Taylor Swift is awesome!"
# 	)

text = Blueprint('text', __name__, template_folder='templates')
				
@text.route('/text/', methods=["GET","POST"])
def text_page():
	if request.method == "POST":
		cursor = db.cursor()
		cursor.execute('SELECT phonenumber FROM users')
		phonen_dict = cursor.fetchall()
		my_test_prompt = request.form['text']
		for numbers in phonen_dict:
			client.messages.create(
				to = numbers['phonenumber'], 
				from_= "+15104221809",
				body= my_test_prompt
			)
	if 'user' in session:
		logged_in = True 
		return render_template('text.html', logged_in = logged_in, username = session['user'], admin = session['admin']) 
	else: 
		logged_in = False 
		return render_template('text.html', logged_in = logged_in)