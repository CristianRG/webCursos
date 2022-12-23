from flask import redirect, render_template, url_for
from templates import app

@app.route('/')
def Index():
    return render_template('app/templates/index.html')

