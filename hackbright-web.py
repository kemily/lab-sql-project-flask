from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get("github")
    first, last, github = hackbright.get_student_by_github(github)
    html = render_template("student_info.html", github=github, first=first, 
                                                last=last)
    return html

@app.route("/student/<github>")
def new_student(github):
    """Show information about a new student, has been added."""

    github = request.args.get(github)
    first, last, github = hackbright.get_student_by_github(github)
    html = render_template("student_info.html", github=github, first=first, 
                                                last=last)
    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student-add-form")
def add_new_student_form():
    """Show form for adding a student."""

    return render_template("student_add.html")

@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""

    first_name = request.form('fname')
    last_name = request.form('lname')
    github = request.form('github')

    hackbright.make_new_student(first_name, last_name, github)
    
    html = render_template("student_confirm.html", first=first_name, 
                                last=last_name, github=github)
    return html

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
