from flask import *

why = Blueprint('why', __name__, template_folder='templates')

@why.route('/why/')
def why_route():
	if 'user' in session:
		logged_in = True
		return render_template('why.html', logged_in = logged_in, username = session['user'])
	else:
		logged_in = False
		return render_template('why.html', logged_in = logged_in)
