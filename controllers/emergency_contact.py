from flask import *

emergency_contact = Blueprint('emergency_contact', __name__, template_folder='templates')

@emergency_contact.route('/emergency_contact/')
def emergency_contact_route():
	if 'user' in session:
		logged_in = True
		return render_template('emergency_contact.html', logged_in = logged_in, username = session['user'])
	else:
		logged_in = False
		return render_template('emergency_contact.html', logged_in = logged_in)
