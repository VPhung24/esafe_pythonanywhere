from flask import *
from extensions import connect_to_database

database = Blueprint('database', __name__, template_folder='templates')

@database.route('/database/')
def database_path():
    db = connect_to_database()
    cur = db.cursor()
    cur.execute('SELECT uid, firstname, lastname, username, city, state, streetaddress, email, password, special_needs, phonenumber, zipcode FROM users')
    results = cur.fetchall()
    print(results)
    print_str = "<table>"
    for result in results:
        print_str += "<tr><td> %s <br></td><td> %s <br></td><td> %s <br></td><td> %s <br></td><td> %s <br></td><td> %s <br></td><td> %s <br></td><td> %s <br></td><td> %s <br></td><td> %s <br></td><td> %s <br></td><td> %s <br></td><tr>" % (result['uid'], result['firstname'], result['lastname'], result['username'], result['city'], result['state'], result['streetaddress'], result['email'], result['password'], result['special_needs'], result['phonenumber'], result['zipcode'])
    print_str += "</table>"
    print(session['logged_in'])
    if 'user' in session:
        logged_in = True
        return render_template("database.html", results = results, logged_in = logged_in, username = session['user'], admin = session['admin'])
    else:
        logged_in = False
        return render_template("database.html", results = results, logged_in = logged_in)


