import json
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
    list = ['Driver ID', 'Car Plate Number', 'Abrupt acceleration times', 'Abrupt Brake Times', 'Neutral Sliding Times', 'Total Neutral Sliding Times (s)', 'Overspeed Times', 'Total Overspeed Times(s)', 'Fatigue Driving TImes', 'Hthrottle Stop Times', 'Oil Leak Times']
    if request.method == 'POST':
        cursor = database.cursor()
        # SELECT DriverID,CarPlateNumber,DATE(recordDAY),sum(isRapidlySpeedup),sum(isRapidlySlowdown),sum(isNeutralSlide),sum(isNeutralSlideFinished),sum(neutralSlideTime),sum(isOverspeed),sum(isOverspeedFinished),sum(overspeedTime),sum(isFatigueDriving),sum(isHthrottleStop),sum(isOilLeak) from `comp4442-group-project`.DrivingRecords  GROUP BY driverID
        # datetime_object = datetime.strptime('2022-04-22 1:32 PM', '%Y-%m-%d %I:%M %p')
        daterange = str(request.form['daterange']).split(' - ', 1)
        start_datetime = str(datetime.strptime(daterange[0], '%Y-%m-%d %I:%M %p'))
        end_datetime = str(datetime.strptime(daterange[1], '%Y-%m-%d %I:%M %p'))
        query = "SELECT DriverID,CarPlateNumber,DATE(recordDAY),sum(isRapidlySpeedup),sum(isRapidlySlowdown),sum(isNeutralSlide),sum(isNeutralSlideFinished),sum(neutralSlideTime),sum(isOverspeed),sum(isOverspeedFinished),sum(overspeedTime),sum(isFatigueDriving),sum(isHthrottleStop),sum(isOilLeak) FROM DrivingRecords WHERE recordDAY between '" + start_datetime + "' AND '" + end_datetime + "' GROUP BY driverID"
        cursor.execute(query)
        results = cursor.fetchall()

        driverID = []
        isRapidlySpeedup=[]
        isRapidlySlowdown=[]
        NeutralSlidingTimes =[]
        TotalNeutralSlidingTimes =[]
        OverspeedTimes = []
        TotalOverspeedTimes =[]
        FatigueDrivingTImes =[]
        HthrottleStopTimes =[]
        OilLeakTimes =[]

        for result in results:
            driverID.append(result[0])
            isRapidlySpeedup.append(result[3])
            isRapidlySlowdown.append(result[4])
            NeutralSlidingTimes.append(result[6])
            TotalNeutralSlidingTimes.append(result[7])
            OverspeedTimes.append(result[9])
            TotalOverspeedTimes.append(result[10])
            FatigueDrivingTImes.append(result[11])
            HthrottleStopTimes.append(result[12])
            OilLeakTimes.append(result[13])
        
        data = [isRapidlySpeedup,isRapidlySlowdown,NeutralSlidingTimes,TotalNeutralSlidingTimes,OverspeedTimes,TotalOverspeedTimes,FatigueDrivingTImes,HthrottleStopTimes,OilLeakTimes]
            
        for i in data:
            print(i)

        return render_template("summary.html", headerList = list,\
                                                results=results,\
                                                driverID=driverID ,\
                                                chart_data = data,\
                                                last_search_value=request.form['daterange'])
         
    else:
        return render_template("summary.html", headerList = list,\
                                                results=[],\
                                                driverID=[] ,\
                                                chart_data = [],\
                                                )



@views.route('/Monitor', methods=['GET', 'POST'])
def monitor():
    driverID = request.args.get('driverID')
    if driverID:
          return render_template("monitor.html", driverID = driverID)
    else:
        return render_template("monitor.html")





@views.route("/data")
def getdata():
    database = connection.connection()
    cur = database.cursor()
    driverID = request.args.get('driverID')
    if driverID:
        sql = "SELECT Time, Speed FROM Monitor WHERE DriverID = '%s'" %(driverID)
        cur.execute(sql)
        datas = []
        for i in cur.fetchall():
            datas.append([i[0], i[1]])

        if len(datas) > 0 :
            tmp_time = datas[-1][0]
            
        return json.dumps(datas)
    else:
        return ""
        