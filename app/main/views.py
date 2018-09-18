from flask import render_template
from .import main

# Views
@main.route('/')
def index():
    '''
    function that returns the index page and its data
    '''

    title = 'LMS-lite Homepage'

    return render_template('index.html', title = title)
    