from flask import *

earthquakes = Blueprint('earthquakes', __name__, template_folder='templates')

@earthquakes.route('/earthquakes/')
def earthquake_route():
	if 'user' in session:
		logged_in = True
		return render_template('earthquakes.html', logged_in = logged_in, username = session['user'])
	else:
		logged_in = False
		return render_template('earthquakes.html', logged_in = logged_in)