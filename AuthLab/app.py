from flask import Flask, render_template, request
from flask import session as login_session
import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyB0fzaKuEKfFlI1Ykm0o6acozFhws_VEY8",
  "authDomain": "authincation-lab.firebaseapp.com",
  "projectId": "authincation-lab",
  "storageBucket": "authincation-lab.appspot.com",
  "messagingSenderId": "724672379450",
  "appId": "1:724672379450:web:f92a0d6538ccea8fe39303"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
app = Flask(__name__, template_folder='templates', static_folder='static')

app.config['SECRET_KEY'] = 'super-secret-key'