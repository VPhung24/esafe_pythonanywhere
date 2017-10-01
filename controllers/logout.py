from flask import *
from extensions import *
logout = Blueprint('logout', __name__, template_folder='templates')

@logout.route('/logout/', methods=["GET","POST"])
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
	return redirect("http://localhost:1989/login/")