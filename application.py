from flask import Flask, render_template
application = Flask(__name__)

@application.route('/')
def hello():
	return render_template("index.html")


@application.route("/about")
def about():
	return render_template("about.html")


@application.route('/resume')
def resume():
    return render_template("resume.html")


@application.route("/projects")
def projects():
	return render_template("project.html")


if __name__ == "__main__":
	application.run()
