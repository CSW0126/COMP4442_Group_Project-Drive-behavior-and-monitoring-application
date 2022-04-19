# example inp and out
# s3://comp4442-group-project/data/
# s3://comp4442-group-project/output

import os
import sys


from pyspark import SparkContext, SQLContext, Row
from pyspark.sql.types import *
from pyspark.sql.functions import lit

args = sys.argv
inp = args[1]
out = args[2]

sc = SparkContext()
sqlContext = SQLContext(sc)

text_file = sc.textFile(inp)

# split each line into a list of fields
# only count the lines that have at least 9 fields, ignore the case that is no special behavior
counts = text_file.map(lambda line: line.split(",")).filter(lambda line: len(line)>8)


column_data = counts.map(lambda p: Row(p[0], p[1], p[2], p[3], p[4], \
                                    p[5], p[6], p[7], p[8], p[9] , \
                                    p[10], p[11], p[12], p[13], p[14], \
                                    p[15], p[16], p[17], p[18]))


column_name = "driverID,carPlateNumber,Latitude,Longitude,Speed,Direction,siteName,Time,isRapidlySpeedup,isRapidlySlowdown,isNeutralSlide,isNeutralSlideFinished,neutralSlideTime,isOverspeed,isOverspeedFinished,overspeedTime,isFatigueDriving,isHthrottleStop,isOilLeak"
sql = "SELECT first(recordID),first(driverID),first(carPlateNumber),first(Time) \
                            as recordDAY,HOUR(Time) as recordHOUR,\
                            sum(isRapidlySpeedup),sum(isRapidlySlowdown),sum(isNeutralSlide),sum(isNeutralSlideFinished),\
                            sum(neutralSlideTime),sum(isOverspeed),sum(isOverspeedFinished),sum(overspeedTime),sum(isFatigueDriving),\
                            sum(isHthrottleStop),sum(isOilLeak) \
                            FROM summary \
                            GROUP BY driverID,DAY(Time),HOUR(Time)"

# create schema with the column names
fields = [StructField(field_name, StringType(), True) for field_name in column_name.split(",")]
schema = StructType(fields)

# apply the schema to the RDD
dataframe = sqlContext.createDataFrame(column_data,schema)
# add the recordID to store where these record come from
dataframe = dataframe.withColumn("recordID",lit(inp))
# register the DataFrame as a table.
dataframe.registerTempTable("summary")

# execute the SQL query and save the result to the output directory
group_data = sqlContext.sql(sql)
group_data.coalesce(1).write.csv(out)

sc.stop()
            