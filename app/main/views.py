from flask import render_template
from .import main
from flask_login import login_required

# Views
@main.route('/')
def index():
    '''
    function that returns the index page and its data
    '''

    title = 'LMS-lite Homepage'

    return render_template('home.html', title = title)
    