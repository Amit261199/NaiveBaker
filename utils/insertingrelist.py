# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 00:37:34 2020

@author: This-PC
"""

import pandas as pd
import psycopg2
df=pd.read_csv('ingredientUsed.csv')
df.fillna('None',inplace=True)
df=df.replace(['None'],[None])



try:
    connection = psycopg2.connect(user = "vwlcjglq",
                                  password = "oxQN469OIA7Xeb_TPeMmqg-wmODUfzkO",
                                  host = "john.db.elephantsql.com",
                                  port = "5432",
                                  database = "vwlcjglq")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    postgres_insert_query = """ INSERT INTO buildpantry_ingredientused (id,quantity,directions,ingredient_name_id,recipe_name_id) VALUES (%s,%s,%s,%s,%s)"""
    count=0
    for i in range(0,df.shape[0]):
        l=list(df.loc[i])
        l[0]=int(l[0])
        record_to_insert = tuple(l)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = count+cursor.rowcount
        print (count, "Record inserted successfully into recipe table")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

