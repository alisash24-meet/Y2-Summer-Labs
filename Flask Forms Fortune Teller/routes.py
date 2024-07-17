from flask import Flask, render_template, redirect, url_for, request
import random 
# import requests

app = Flask(__name__, template_folder = "templates",static_folder = "static")

@app.route("/home", methods=['GET','POST'])
def home():
	if request.method == 'POST':
		answer = request.form['answer']
		return redirect(url_for('fortune', answer = answer))

	return render_template("home.html")

@app.route("/fortune/<string:answer>")
def fortune(answer):
	birth_month = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
	if answer.upper() in birth_month:
		fortune_list = ["You will have IASA food", "You will have DU", "You will have CS", "You will have Entrep", "Lilach the dragon will befriend you", "You will not have hot water in the dorm", "You will eat a muffin", "You will win a smiley sticker", "You will have a voice crack", "Abdallah will be angry at you"]
		#random_indx = random.randint(0, 9)
		return render_template("fortune.html", fortune = fortune_list[len(answer)])
	return redirect(url_for('home'))



if __name__ == "__main__":
	app.run(debug = True)