from flask import Flask, escape, request, render_template, flash, redirect, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '034e6e1b7628c772357906be031cdbd8'

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
