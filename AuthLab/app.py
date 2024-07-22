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
    email = request.form["email"]
    password= request.form["password"]
    login_session["quotes"]=[]
    try:
      login_session['user']= auth.create_user_with_email_and_password(email, password)
      return redirect(url_for('home')) 
    except:
      print("Authentication failed :(")
      return redirect('error')



@app.route("/signin", methods=['POST','GET'])
def sign_in():
  if request.method == 'GET':
    return render_template('signin.html')
  else:
    email = request.form["email"]
    password= request.form["password"]
    login_session["quotes"]=[]
    try:
      login_session['user'] = auth.sign_in_with_email_and_password(email, password)
      return redirect(url_for('home')) 
    except:
       print("This user does not exist.")
       return redirect(url_for('error'))

@app.route('/signout')
def signout():
  login_session['user'] = None
  auth.current_user = None
  return redirect(url_for('sign_in'))

@app.route("/home", methods=['POST','GET'])
def home():
  if request.method == 'GET':
    return render_template('home.html')
  else:
    login_session["quotes"].append(request.form["quote"])
    login_session.modified = True
    return redirect(url_for('thanks'))

@app.route("/thanks")
def thanks():
  return render_template('thanks.html')

@app.route("/display")
def display():
  if request.method == 'GET':
    return render_template('display.html',quotes=login_session["quotes"])

@app.route("/error")
def error():
  if request.method == 'GET':
    return render_template('error.html')




if __name__ == '__main__':
  app.run(debug=True)