
import mysql.connector
from mysql.connector import Error

try:
    db = mysql.connector.connect(host='localhost',
                                         database='cripto',
                                         user='lbisaro',
                                         password='Fmn361612')
    if db.is_connected():
        db_Info = db.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = db.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if db.is_connected():
        cursor.close()
        db.close()
        print("MySQL connection is closed")
