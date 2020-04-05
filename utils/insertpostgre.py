import pandas as pd
import psycopg2
import datetime
df=pd.read_excel('xl.xlsx')
df.fillna('None',inplace=True)
df=df.replace(['None'],[None])

df['timetocook']=df['timetocook'].map(lambda x: datetime.timedelta(hours=int(x.split(':')[0]),minutes=int(x.split(':')[1])))


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
    postgres_insert_query = """ INSERT INTO buildpantry_recipe (title, description,instructions,cuisine,dishtype,mark,images,timetocook,mealtype) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    count=0
    for i in range(df.shape[0]):
        record_to_insert = tuple(df.loc[i])
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

