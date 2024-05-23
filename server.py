import mysql.connector
from mysql.connector import Error



try:
    conn = mysql.connector.connect(host = "localhost", 
                                   database = "desktopdb", 
                                   user = "root", password = "")
    print("Connection Successfully Established!")

except Error as e:
    print("Connection Error!", e)