from flask import Flask
from flask import render_template
from flask import redirect, request

app = Flask(__name__)
APP_VERSION = '0.0.1'

@app.route('/') # Defines the route the page will be served on
def home():
    return render_template('home.html')

@app.route('/guess') # Defines the route the page will be served on
def guess():
    return render_template('guess.html')

@app.route('/upload_image') # Defines the route the page will be served on
def upload_image():
    return render_template('upload_image.html')

@app.route('/words') # Defines the route the page will be served on
def words():
    return render_template('words.html')

@app.context_processor
def inject_app_version():
    return dict(app_version=APP_VERSION)

@app.route('/upload_word', methods=['POST'])  # browsers send POST request when submitting a form
def upload_word():
    # request.form is a special variable in Flask that will contain the form data
    secret_word = request.form['secretWord']  # note the "name" attribute of the <input> we have in HTML
    print("Uploaded word " + repr(secret_word))
    return redirect('/')  # redirect back to the main page