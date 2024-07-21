from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session
import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyB0fzaKuEKfFlI1Ykm0o6acozFhws_VEY8",
  "authDomain": "authincation-lab.firebaseapp.com",
  "projectId": "authincation-lab",
  "storageBucket": "authincation-lab.appspot.com",
  "messagingSenderId": "724672379450",
  "appId": "1:724672379450:web:f92a0d6538ccea8fe39303",
  "databaseURL":""
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
app = Flask(__name__, template_folder='Templates', static_folder='static')

app.config['SECRET_KEY'] = 'super-secret-key'

@app.route("/",methods= ['POST','GET'])
def sign_up():
  if request.method == 'GET':
    return render_template('signup.html')
  else:
    login_session["email"] = request.form["email"]
    login_session["password"]= request.form["password"]
    login_session["quotes"]=[]
    return redirect(url_for('home')) 


@app.route("/signin")
def sign_in():
  if request.method == 'GET':
    return render_template('signin.html')
  else:
    login_session["email"] = request.form["email"]
    login_session["password"]= request.form["password"]
    login_session["quotes"]=[]
    return redirect(url_for('home')) 

@app.route("/signout")
def sign_out():
  return render_template('sign_out')

@app.route("/home")
def home():
  return render_template('home.html')

@app.route("/thanks")
def thanks():
  return render_template('thanks.html')

@app.route("/display")
def display():
  return render_template('display.html')

if __name__ == '__main__':
  app.run(debug=True)