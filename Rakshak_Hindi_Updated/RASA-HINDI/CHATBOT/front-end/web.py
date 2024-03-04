from flask import Flask 
from flask import render_template, request, redirect, session, url_for
import json
import os

import re
  
# creates a Flask application 
app = Flask(__name__) 

app.secret_key = 'xyzsdfg'
  
  
@app.route("/") 
@app.route('/login', methods =['GET', 'POST'])
def login():
    # if session.get('loggedin'):
    #     return render_template('index.html', message=session.get('name', ''))
    
    message = ''
    account = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not os.path.exists('./user_details.json'):
            with open('./user_details.json', 'w') as file:
                json.dump({}, file)
                
        with open('./user_details.json', 'r') as fin:
            user_account_details = json.load(fin)
            # print(user_account_details)
            if username in user_account_details.keys():
                account = user_account_details[username]
        # if account exists in our DB
        if account and password == account[0] and username != '':
            # creating session
            session['loggedin'] = True
            session['username'] = username
            session['name'] = account[1]
            name = account[1]
            message = 'Logged in successfully !'
            return render_template('index.html', message = name)
        else:
            message = 'Please enter correct username / password !'
    return render_template('login.html', message = message)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/register', methods =['GET', 'POST'])
def register():
    message = ''
    account = None 

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conf_password = request.form['cpassword']
        fname = request.form['fname']
        lname = request.form['lname']
        name = fname + " " + lname
        
        # checking whether the user already exists in the DB
        if not os.path.exists('./user_details.json'):
            with open('./user_details.json', 'w') as file:
                json.dump({}, file)
            
        with open('./user_details.json', 'r') as fin:
            # print(username, password, email, organization)
            data = {username: [password, name]}
            user_account_details = json.load(fin)
            
            # print(user_account_details)
            if username in user_account_details.keys():
                account = True

        if account:
            message = 'Username already exists! Please try a different one'
        # elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        #     message = 'Invalid email address !'
        elif password != conf_password:
            message = 'The password entered in the Confirm Password field does not match the original Password'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        else:
            with open('./user_details.json', 'r+') as fin:
                # print(username, password, email, organization)
                data = {username: [password, name]}
                print(data)
                json_data = json.load(fin)
                json_data.update(data)
                fin.seek(0)
                json.dump(json_data, fin)
    
            message = 'You have successfully registered ! Please Login to proceed'
            return redirect(url_for('login'))
    elif request.method == 'POST':
        message = 'Please fill out the form !'
    return render_template('register.html', message = message)
  
# run the application 
if __name__ == "__main__": 
    app.run(host='0.0.0.0', port=5089, debug=True)

    