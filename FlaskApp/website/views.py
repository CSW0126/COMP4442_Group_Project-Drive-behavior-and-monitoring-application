from flask import Blueprint, render_template

views = Blueprint('views', __name__)

# define url

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/Summary')
def summary():
    return render_template("summary.html")

@views.route('/Monitor')
def monitor():
    return render_template("monitor.html")


