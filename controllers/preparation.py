from flask import *

preparation = Blueprint('preparation', __name__, template_folder='templates')

@preparation.route('/preparation/')
def preparation_route():
	if 'user' in session:
		logged_in = True 
		return render_template('preparation.html', logged_in = logged_in, username = session['user']) 
	else: 
		logged_in = False 
		return render_template('preparation.html', logged_in = logged_in)
