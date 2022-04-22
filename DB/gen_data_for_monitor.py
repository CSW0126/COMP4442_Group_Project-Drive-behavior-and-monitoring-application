import random
import time
from connection import connection

def generate_data():
    DriverID = 'COMP4442'
    Speed = 1*random.randint(0,10)+ 10*random.randint(5,7)
    #Speed = 1*random.randint(0,10)+ 10*random.randint(8,10)  
    Time = int(time.time())
    data = [DriverID,Speed,Time]

    return data

def main():
    db_conn = connection()
    cursor = db_conn.cursor()

    while True:
        data = generate_data()
        sql = "INSERT INTO Monitor (DriverID, Speed, Time) values(%s, %s, %s);"
        cursor.execute(sql, data)
        db_conn.commit()
        time.sleep(1)
        print("Insert data to database", data)


if __name__ == '__main__':
    main()




