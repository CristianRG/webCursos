from flask import redirect, render_template, url_for
from run import app

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/courses/')
def getCourses():
    return render_template('courses.html')

@app.route('/courses/<string:course>')
def getCourse(course):
    return render_template('courses/{}/course-{}.html'.format(course, course))