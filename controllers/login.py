from flask import *
from extensions import *
login = Blueprint('login', __name__, template_folder='templates')



@login.route('/login/', methods=["GET","POST"])
def login_page():

  # session.pop('user', None)

  if request.method == "POST":
    attempted_username = request.form['username']
    attempted_password = request.form['password']

    cursor = db.cursor()
    cursor.execute('SELECT username FROM users WHERE username = %s', (attempted_username))
    test_for_username = cursor.fetchall()
    error = '' # if username exists, test that the password matches
    if not test_for_username:
      error = "Invalid credentials. Try Again."
      session['logged_in'] = False
      return render_template("login.html", error = error, logged_in = session['logged_in'])  
    else:
      if not attempted_password:
        error = "Invalid credentials. Try Again."
        session['logged_in'] = False
        return render_template("login.html", error = error, logged_in = session['logged_in'])  
      else:
        cursor = db.cursor()
        cursor.execute('SELECT password FROM users WHERE username = %s', (attempted_username))
        results = cursor.fetchall()
        print(results)
        print(attempted_password)
        results = results[0]['password']

        if results == attempted_password:
          session['logged_in'] = True
          session['user'] = request.form['username']
         

          #firstname
          cursor.execute('SELECT firstname FROM users WHERE username = %s', (attempted_username))
          firstname_dict = cursor.fetchall()
          session['firstname'] = firstname_dict[0]['firstname']

          #lastname
          cursor.execute('SELECT lastname FROM users WHERE username = %s', (attempted_username))
          lastname_dict = cursor.fetchall()
          session['lastname'] = lastname_dict[0]['lastname']

          #city
          cursor.execute('SELECT city FROM users WHERE username = %s', (attempted_username))
          city_dict = cursor.fetchall()
          session['city'] = city_dict[0]['city']

          #zipcode
          cursor.execute('SELECT zipcode FROM users WHERE username = %s', (attempted_username))
          zipcode_dict = cursor.fetchall()
          session['zipcode'] = zipcode_dict[0]['zipcode']
          
          #state
          cursor.execute('SELECT state FROM users WHERE username = %s', (attempted_username))
          state_dict = cursor.fetchall()
          session['state'] = state_dict[0]['state']

          #streetaddress
          cursor.execute('SELECT streetaddress FROM users WHERE username = %s', (attempted_username))
          streetaddress_dict = cursor.fetchall()
          session['streetaddress'] = streetaddress_dict[0]['streetaddress']
          
          #email
          cursor.execute('SELECT email FROM users WHERE username = %s', (attempted_username))
          email_dict = cursor.fetchall()
          session['email'] = email_dict[0]['email']

          #special needs
          cursor.execute('SELECT special_needs FROM users WHERE username = %s', (attempted_username))
          specialneeds_dict = cursor.fetchall()
          session['special_needs'] = specialneeds_dict[0]['special_needs']

          #phonenumber
          cursor.execute('SELECT phonenumber FROM users WHERE username = %s', (attempted_username))
          phonenumber_dict = cursor.fetchall()
          session['phonenumber'] = phonenumber_dict[0]['phonenumber']

          #admin
          cursor.execute('SELECT uid FROM users WHERE username = %s', (attempted_username))
          uid_dict = cursor.fetchall()
          uid = uid_dict[0]['uid']
          admin = False

          #test
          cursor.execute('SELECT phonenumber FROM users')
          phonen_dict = cursor.fetchall()
          print(phonen_dict)

          if uid < 30:
            admin = True
            session['admin'] = True
          else:
            admin = False
            session['admin'] = False
          return render_template("login.html", firstname = session['firstname'], lastname = session['lastname'], city = session['city'], username = session['user'], zipcode = session['zipcode'], state = session['state'], streetaddress = session['streetaddress'], email = session['email'], logged_in = session['logged_in'], admin = session['admin'], phonenumber =  session['phonenumber'], specialneeds = session['special_needs'])  # this is the valid password and username
        else:
          session['logged_in'] = False
          error = "Invalid credentials. Try Again."
          return render_template("login.html", error = error, logged_in = session['logged_in'])  #otherwise it is wrong
  elif 'user' in session:
    return render_template("login.html", firstname = session['firstname'], lastname = session['lastname'], city = session['city'], username = session['user'], zipcode = session['zipcode'], state = session['state'], streetaddress = session['streetaddress'], email = session['email'], logged_in = session['logged_in'], admin = session['admin'], phonenumber =  session['phonenumber'], specialneeds = session['special_needs'])  
  else:
    session['logged_in'] = False
    return render_template("login.html")  

