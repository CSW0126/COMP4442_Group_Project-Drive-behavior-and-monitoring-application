from flask import Blueprint, render_template, request
import sys
import os
from datetime import datetime
sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../../')))
from DB import connection
views = Blueprint('views', __name__)

database = connection.connection()

# define url


@views.route('/')
def home():
    return render_template("home.html")


@views.route('/Summary', methods=['GET', 'POST'])
def summary():
    if request.method == 'POST':
        cursor = database.cursor()
        # SELECT DriverID,CarPlateNumber,DATE(recordDAY),sum(isRapidlySpeedup),sum(isRapidlySlowdown),sum(isNeutralSlide),sum(isNeutralSlideFinished),sum(neutralSlideTime),sum(isOverspeed),sum(isOverspeedFinished),sum(overspeedTime),sum(isFatigueDriving),sum(isHthrottleStop),sum(isOilLeak) from `comp4442-group-project`.DrivingRecords  GROUP BY driverID
        # datetime_object = datetime.strptime('2022-04-22 1:32 PM', '%Y-%m-%d %I:%M %p')
        daterange = str(request.form['daterange']).split(' - ', 1)
        start_datetime = str(datetime.strptime(daterange[0], '%Y-%m-%d %I:%M %p'))
        end_datetime = str(datetime.strptime(daterange[1], '%Y-%m-%d %I:%M %p'))
        query = "SELECT DriverID,CarPlateNumber,DATE(recordDAY),sum(isRapidlySpeedup),sum(isRapidlySlowdown),sum(isNeutralSlide),sum(isNeutralSlideFinished),sum(neutralSlideTime),sum(isOverspeed),sum(isOverspeedFinished),sum(overspeedTime),sum(isFatigueDriving),sum(isHthrottleStop),sum(isOilLeak) FROM DrivingRecords WHERE recordDAY between '" + start_datetime + "' AND '" + end_datetime + "' GROUP BY driverID"
        cursor.execute(query)
        result = cursor.fetchall()
        return render_template("summary.html", results=result, last_search_value=request.form['daterange'])
    else:
        return render_template("summary.html")


@views.route('/Monitor')
def monitor():
    return render_template("monitor.html")
