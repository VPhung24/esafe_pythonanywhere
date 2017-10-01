from flask import *

wildfires = Blueprint('wildfires', __name__, template_folder='templates')

@wildfires.route('/wildfires/')
def wildfires_route():
	if 'user' in session:
		logged_in = True 
		return render_template('wildfires.html', logged_in = logged_in, username = session['user'])
	else:
		logged_in = False
		return render_template('wildfires.html', logged_in = logged_in)