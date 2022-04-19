# comp4442-group-project.coa9uj3ys1py.us-east-1.rds.amazonaws.com
# port 3306
# username: admin
# password: 12345678
# database: comp4442-group-project


import mysql.connector
import pandas as pd

host = "comp4442-group-project.coa9uj3ys1py.us-east-1.rds.amazonaws.com"
user = "admin"
password = "12345678"
port = 3306
database = "comp4442-group-project"


def upload_data_to_DB():
    # connect to database
    # mydb = mysql.connector.connect(
    #     host=host,
    #     user=user,
    #     passwd=password,
    #     database=database,
    #     port=port
    # )

    #data frames list
    dfs = []

    # read data from csv file
    #df1 = pd.read_csv(f"../detail-records/detail_record_2017_01_02_08_00_00")
    #df2 = pd.read_csv(f"../detail-records/detail_record_2017_01_03_08_00_00")
    #df3 = pd.read_csv(f"../detail-records/detail_record_2017_01_04_08_00_00")
    #df4 = pd.read_csv(f"../detail-records/detail_record_2017_01_05_08_00_00")
    #df5 = pd.read_csv(f"../detail-records/detail_record_2017_01_06_08_00_00")
    #df6 = pd.read_csv(f"../detail-records/detail_record_2017_01_07_08_00_00")
    #df7 = pd.read_csv(f"../detail-records/detail_record_2017_01_08_08_00_00")
    #df8 = pd.read_csv(f"../detail-records/detail_record_2017_01_09_08_00_00")
    #df9 = pd.read_csv(f"../detail-records/detail_record_2017_01_10_08_00_00")
    #df10 = pd.read_csv(f"../detail-records/detail_record_2017_01_11_08_00_00")



    
    # print(df)

if __name__ == "__main__":
    upload_data_to_DB()

