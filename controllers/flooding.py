from flask import *

flooding = Blueprint('flooding', __name__, template_folder='templates')

@flooding.route('/flooding/')
def flooding_route():
	if 'user' in session:
		logged_in = True
		return render_template("flooding.html" , logged_in = logged_in, username = session['user'])
	else:
		logged_in = False
		return render_template("flooding.html" , logged_in = logged_in)