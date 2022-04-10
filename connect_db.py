import pymysql  

def connect(query):
    con = pymysql.connect(host="localhost",user="root",database="LMS")
    cur=con.cursor()
    result=cur.execute(query)
    con.commit()
    return result
