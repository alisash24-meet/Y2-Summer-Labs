from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session
import pyrebase
import firebase
import random


firebaseConfig = {
  "apiKey": "AIzaSyBn11SA1opXzaxXZR78wS6xHnylc3PhYc0",
  "authDomain": "lanawebsite-302eb.firebaseapp.com",
  "projectId": "lanawebsite-302eb",
  "storageBucket": "lanawebsite-302eb.appspot.com",
  "messagingSenderId": "115671276714",
  "appId": "1:115671276714:web:4c5e9dccef6ed5b227c4d3",
  "measurementId": "G-B48HD7P0KM",
  "databaseURL": "https://lanawebsite-302eb-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth = firebase.auth()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

lana_facts=["Lana's real name is Elizabeth Woolridge Grant.","Lana studied metaphysics in college.","Lana has a tatto of the letter M in honor of her grandmother.","Lana was born on the 21st of June, 1985.","Her first stage name was May Jailer.","Lana has been nominated for 6 Grammy Awards and a Golden Globe Award.","Lana has two apartments, one in New York and the other in L.A. where she lives with her brother and sister."]
lana_del=[" Pray"," Slay"," Tray"," Neigh"," Clay"," Lay"," Bay"]

@app.route("/", methods=['POST','GET'])
def home():
   return render_template('home.html')

@app.route("/signin" , methods=['POST', 'GET'])
def sign_in():
  if request.method == 'GET':
    return render_template('signin.html')
  else:
    email = request.form["email"]
    password= request.form["password"]
    username= request.form["username"]
    try:
      login_session['user'] = auth.sign_in_with_email_and_password(email, password, username)
      return redirect(url_for('options')) 
    except:
       print("This user does not exist.")
       return redirect(url_for('error'))

@app.route("/signup", methods=['POST','GET'])
def sign_up():
	if request.method == 'GET':
		return render_template('signup.html')
	else:
	    email = request.form["email"]
	    password= request.form["password"]
#	    fullname= request.form["fullname"]
	    username= request.form["username"]
	    user = {"password": password, "username": username,"email": email}
	    try:
	      user = {"password": password, "username": username,"email": email}
	      login_session['user']= auth.create_user_with_email_and_password(email, password)
	      UID=login_session['user']['localId']
	      db.child("Users").child(UID).set(user)
	      return redirect(url_for('options')) 
	    except:
	      print("Authentication failed :(")
	      return redirect('error')

@app.route("/options", methods=['POST','GET'])
def options():
	return render_template('options.html')

@app.route("/songs", methods=['POST','GET'])
def songs():
	return render_template('songs.html')

@app.route("/random", methods=['POST','GET'])
def randomized():
	if request.method == 'POST':
		button1 = request.form["button"]
		print(button1)
		chosen_fact=""
		chosen_lana=""
		if button1 =="Random Fact:":
			chosen_fact=lana_facts [random.randint(0, 6)]
		else:
			chosen_lana=lana_del [random.randint(0,6)]
		return render_template('random.html',chosen_fact2 = chosen_fact, chosen_lana2 = chosen_lana)
	else:
		return render_template('random.html')

@app.route('/signout')
def signout():
  login_session['user'] = None
  auth.current_user = None
  return redirect(url_for('home'))

@app.route('/profile', methods=['POST','GET'])
def profile():
	return render_template('profile.html')

@app.route('/bio', methods=['POST','GET'])
def bio():
	if request.method == 'GET':
		return render_template('bio.html')
	else:
		input1=[]
		quote = request.form["quote"]
		input1.append(quote)
		user["quote"]=quote
		db.child("Users").child(UID).set(user)


@app.route('/error', methods=['POST','GET'])
def error():
	return render_template('error.html')




if __name__ == '__main__':
  app.run(debug=True)