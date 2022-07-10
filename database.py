from mysql.connector import connect

db = connect(host="localhost", username="root", password="", database="lms")
dbstore = connect(host="localhost", username="root", password="", database="lms")
dbstudents = connect(host="localhost", username="root", password="", database="lms")