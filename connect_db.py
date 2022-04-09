import pymysql  

def connect():
    con = pymysql.connect(host="localhost",user="root",database="LMS")
    return con
