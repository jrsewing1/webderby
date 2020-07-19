from datetime import datetime
from flask import Flask, escape, request, render_template, flash, redirect, url_for
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '034e6e1b7628c772357906be031cdbd8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Driver(db.Model):
		id = db.Column(db.Integer, primary_key=True)
		drivername = db.Column(db.String(30), unique=True, nullable=False)
		email = db.Column(db.String(120), unique=True, nullable=False)
		immage_file = db.Column(db.String(20), nullable=False, default='default.jpg')
		password = db.Column(db.String(60), nullable=False)

		def __repr__(self):
			return f"Driver('{self.drivername}', '{self.email}', '{self.image_file}')"

class Cars(db.Model):
		id = db.Column(db.Integer, primary_key=True)
		car_name = db.Column(db.String(30), unique=True, nullable=False)
		weight = db.Column(db.String(30), unique=True, nullable=False)

		def __repr__(self):
			return f"Driver('{self.car_name}', '{self.weight})"

cars = [
	{
		'car': 'Car 1',
		'driver': 'Ross Ewing',
		'lane': '1'
	},
	{
		'car': 'Car 2',
		'driver': 'Abigail Lalande',
		'lane': '2'
	},
	{
		'car': 'Car 3',
		'driver': 'Anthony Lalande',
		'lane': '3'
	}	
]


#Routes
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', cars=cars)

@app.route('/about')
def about():
	return render_template('about.html', title='About')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('registration.html', title='Registration', form=form)

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)	

@app.route('/setup')
def setup():
	return render_template('setup.html', title='About')

#conditional to run from python in debug mode
if __name__ == '__main__':
	app.run(debug=True)
