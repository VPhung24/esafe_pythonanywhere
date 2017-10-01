from flask import *

landslides = Blueprint('landslides', __name__, template_folder='templates')

@landslides.route('/landslides/')
def landslides_route():
	if 'user' in session:
		logged_in = True
		return render_template('landslides.html', logged_in = logged_in, username = session['user'])
	else:
		logged_in = False
		return render_template('landslides.html', logged_in = logged_in)