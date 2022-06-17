
#from mzroad_django.bigdata.bigDataProcess import process_bigdata
import numpy as np

from bigDataProcess import process_bigdata

import pandas as pd 
import pymysql

from process_AI import process_AI

conn=pymysql.connect(host="mzroad-mysql.c7fq71egwjvc.us-west-2.rds.amazonaws.com",
                     user="root",
                     password="toor1234",
                     db='mzroad',
                     charset='utf8')

curs = conn.cursor()

bigdata_update_sql = "UPDATE test_app_test SET final_result=%s WHERE final_result =%s"

AI_update_sql = "UPDATE test_app_test SET final_result=%s WHERE final_result IS NULL"



sql="select * from test_app_test"
curs.execute(sql)
rows = curs.fetchall()
df=pd.DataFrame(rows, columns=('id','feelings_action', 'tendencies','facial_result','final_result'))




for i in range(70,df.shape[0]):
    if df['final_result'][i] == "null":
        result = process_bigdata(df)
        curs.execute(bigdata_update_sql, (result, "null"))
        conn.commit()

    if df['final_result'][i] == None:
        print(i)
        result = process_AI(df)
        curs.execute(AI_update_sql, (result))
        conn.commit()

    # if df["tendencies"][i] == "null":
    #
    #     result = process_AI(df)
    #     curs.execute(AI_update_sql, (result,"null"))
    #     conn.commit()


conn.close()
