from flask import *

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def main_route():
    if 'user' in session:
        logged_in = True
        return render_template('index.html', logged_in = logged_in, username = session['user'])
    else:
        logged_in = False
        return render_template('index.html', logged_in = logged_in)