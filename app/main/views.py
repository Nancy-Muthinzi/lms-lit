from flask import render_template,redirect,url_for,abort
from .import main
from ..models import User
from flask_login import login_required

# Views
@main.route('/')
def index():
    '''
    function that returns the index page and its data
    '''

    title = 'LMS-lite Homepage'

    return render_template('home.html', title = title)

# @main.route('/')
# def content():
# 	text = open('.textfile.txt', 'r+')
# 	content = text.read()
# 	text.close()
# 	return render_template('content.html', text=content)
 
# @main.route('/user/<uname>')
# def profile(uname):
#     user = User.query.filter_by(username = uname).first()

#     if user is None:
#         abort(404)

#     return render_template("profile/profile.html", user = user)