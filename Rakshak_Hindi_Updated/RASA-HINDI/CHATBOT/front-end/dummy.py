from flask import Flask 
from flask import render_template, request, redirect, session, url_for
# from flaskext.mysql import MySQL
# import MySQLdb.cursors
import re
  
# creates a Flask application 
app = Flask(__name__) 

app.secret_key = 'xyzsdfg'
  
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'Rakshak'
  
# mysql = MySQL(app)
  
@app.route("/") 
@app.route('/login', methods =['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # cursor.execute('SELECT * FROM user WHERE Username = % s AND Password = % s', (username, password, ))
        # user = cursor.fetchone()
        user = True
        if user:
            # session['loggedin'] = True
            # #session['userid'] = user['userid']
            # session['name'] = user['Name']
            # name = user['name']
            # session['username'] = user['Username']
            name = "Rishikant"
            message = 'Logged in successfully !'
            return render_template('index.html', message = name)
        else:
            message = 'Please enter correct email / password !'
    return render_template('login.html', message = message)

@app.route('/logout')
def logout():
    # session.pop('loggedin', None)
    # session.pop('username', None)
    # session.pop('name', None)
    return redirect(url_for('login'))

@app.route('/register', methods =['GET', 'POST'])
def register():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conf_password = request.form['cpassword']
        fname = request.form['fname']
        lname = request.form['lname']
        name = fname + " " + lname
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # cursor.execute('SELECT * FROM user WHERE Username = %s', (username))
        # account = cursor.fetchone()
        account =False
        if account:
            message = 'Username already exists! Please try a different one'
        # elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        #     message = 'Invalid email address !'
        elif password != conf_password:
            message = 'The password entered in the Confirm Password field does not match the original Password'
        else:
            # cursor.execute('INSERT INTO user VALUES ( % s, % s, % s)', (username, password, name))
            # mysql.connection.commit()
            message = 'You have successfully registered ! Please Login to proceed'
            return redirect(url_for('login'))
    elif request.method == 'POST':
        message = 'Please fill out the form !'
    return render_template('register.html', message = message)
  
# run the application 
if __name__ == "__main__": 
    app.run(host='0.0.0.0', port=5083, debug=True)

    