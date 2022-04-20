# comp4442-group-project.coa9uj3ys1py.us-east-1.rds.amazonaws.com
# port 3306
# username: admin
# password: 12345678
# database: comp4442-group-project

# use initDB.sql before run this script

from connection import connection
import numpy as np
import pandas as pd

sql = "INSERT INTO DrivingRecords (DriverID,\
                                   CarPlateNumber,\
                                   recordDAY,\
                                   recordHour,\
                                   isRapidlySpeedup,\
                                   isRapidlySlowdown,\
                                   isNeutralSlide,\
                                   isNeutralSlideFinished,\
                                   neutralSlideTime,\
                                   isOverspeed,\
                                   isOverspeedFinished,\
                                   overspeedTime,\
                                   isFatigueDriving,\
                                   isHthrottleStop,\
                                   isOilLeak) \
                                   values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
sql_delete_All_rows = "DELETE FROM DrivingRecords;"
sql_reset_auto_increment = "ALTER TABLE DrivingRecords AUTO_INCREMENT = 1;"



def main():
    #data frames list
    df = pd.read_csv("../data-after-spark/data.csv", header=None)
    df = df.replace({np.nan: None})


    db_conn = connection()
    cursor = db_conn.cursor()
    
    # delete all rows before insert new data
    cursor.execute(sql_delete_All_rows)
    db_conn.commit()
    print("Delete all rows before insert new data")

    # reset auto increment
    cursor.execute(sql_reset_auto_increment)
    db_conn.commit()
    print("Reset auto increment to 1")

    # insert data to database
    print("Insert data to database")

    dataList = []
    # for each row in data frame
    for index, rows in df.iterrows():
        data = rows.tolist()
        dataList.append(data)
        # print("Process: [{}/{}]".format(index+1, len(df)))
    cursor.executemany(sql, dataList)
    db_conn.commit()

    cursor.close()
    db_conn.close()


    
    # print(df)

if __name__ == "__main__":
    main()

