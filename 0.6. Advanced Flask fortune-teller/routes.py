from flask import Flask, render_template
import random 

app = Flask(__name__, template_folder = "templates",static_folder = "static")

@app.route("/home")
def home():
	return render_template("home.html")

@app.route("/fortune")
def fortune():
	fortune_list = ["You will have IASA food", "You will have DU", "You will have CS", "You will have Entrep", "Lilach the dragon will befriend you", "You will not have hot water in the dorm", "You will eat a muffin", "You will win a smiley sticker", "You will have a voice crack", "Abdallah will be angry at you"]
	Random_indx = random.randint(0, 9)
	return render_template("fortune.html", fortune = fortune_list[Random_indx])

if __name__ == "__main__":
	app.run(debug = True)