from re import X
import time
from typing import final
import numpy as np
import pandas as pd

from connection import connection


def main():
    
    data0 = "~\Documents\GitHub\COMP4442_Group_Project\detail-records\detail_record_2017_01_02_08_00_00"
    
    data1 = "~\Documents\GitHub\COMP4442_Group_Project\detail-records\detail_record_2017_01_03_08_00_00"

    data2 = "~\Documents\GitHub\COMP4442_Group_Project\detail-records\detail_record_2017_01_04_08_00_00"

    data3 = "~\Documents\GitHub\COMP4442_Group_Project\detail-records\detail_record_2017_01_05_08_00_00"

    data4 = "~\Documents\GitHub\COMP4442_Group_Project\detail-records\detail_record_2017_01_06_08_00_00"

    data5 = "~\Documents\GitHub\COMP4442_Group_Project\detail-records\detail_record_2017_01_07_08_00_00"

    data6 = "~\Documents\GitHub\COMP4442_Group_Project\detail-records\detail_record_2017_01_08_08_00_00"

    data7 = "~\Documents\GitHub\COMP4442_Group_Project\detail-records\detail_record_2017_01_09_08_00_00"
 
    data8 = "~\Documents\GitHub\COMP4442_Group_Project\detail-records\detail_record_2017_01_10_08_00_00"
  
    data9 = "~\Documents\GitHub\COMP4442_Group_Project\detail-records\detail_record_2017_01_11_08_00_00"
    
    dataList = [data0,data1,data2,data3,data4,data5,data6,data7,data8,data9]

    data_col = ['driverID', 'speed', 'time', 'carNumber']
    colnames=['driverID', 'carNumber', 'latitude', 'longitude','speed','direction',"siteName","time","isRapidlySpeedup","isRapidlySlowdown","isNeutralSlide","isNeutralSlideFinished","neutralSlideTime","isOverspeed","isOverspeedFinished","overspeedTime","isFatigueDriving","isHthrottleStop","isOilLeak"] 
    dfList = []
    for dataPath in dataList:
        data = pd.read_csv(dataPath, names = colnames ,header=None, index_col=False, usecols=data_col)
        data = data.replace({np.nan: None})
        dfList.append(data)

    
    db_conn = connection()
    cursor = db_conn.cursor()
    SQLdata = []
    for i in range(0, len(dfList)):       
        for j in range(0, len(dfList[i])): 
            SQLdata.append((str(dfList[i].iloc[j,0]), str(dfList[i].iloc[j,1]), str(dfList[i].iloc[j,2]), str(dfList[i].iloc[j,3])))
            
    
    sql = "INSERT INTO MonitorOldData (driverID, CarPlateNumber,  Speed, recordDay ) values(%s, %s, %s, %s);"
    cursor.executemany(sql, SQLdata)
    db_conn.commit()
    print(SQLdata)
    

    

 #data = ( str(dfList[i].iloc[j,0]), str(dfList[i].iloc[j,1]), str(dfList[i].iloc[j,2]))

if __name__ == "__main__":
    main()