from flask import render_template
from flask_login import login_required

from . import home

@home.route('/')
def homepage():
    """
    Render the homepage
    """
    return render_template('home/index.html', title='Welcome')


@home.route('/about')
def about():
    """
    Render the about page
    """
    return render_template('home/about.html', title='About')


@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Dashboard")