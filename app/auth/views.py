from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from forms import LoginForm, RegistrationForm
from .. import db
from ..models import User

@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register route
    Add a User to the database through the registration form
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                            username=form.username.data,
                            first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            pw=form.password.data)

        # add user to the database
        db.session.add(user)
        db.session.commit()
        flash('You have successfully registered! You may now login.')

        # redirect to the login page
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form, title='Register')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log a user in through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():
        # check whether User exists in the database and whether
        # the password entered matches the password in the database
        user = User.query.filter_by(email=form.email.data).first_or_404()
        print user.username
        print "Form pass: %s", form.password.data
        print "Actual pass: %s", user._password
        if user.verify_password(form.password.data):
            login_user(user)
            print "Login Success"
            next = flask.request.args.get('next')   # Page user was trying to access
            
            # is_safe_url should check if the url is safe for redirects.
            if not is_safe_url(next):
                return flask.abort(400)

            return flask.redirect(next or flask.url_for('home.dashboard'))
            #return redirect(url_for('home.dashboard'))

        # when login details are incorrect
        else:
            print "Login Fail"
            flash('Invalid email or password.')

    # load login template
    return render_template('auth/login.html', form=form, title='Login')


@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log a user out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('auth.login'))