import mysql.connector as mysql
import json

db = None
listconfig = []

def dataconnection(shost, suser, spass, sdb):
    global db
    db = mysql.connect(
        host = shost,
        user = suser,
        passwd = spass,
        database = sdb
        )
    
def getdataconfig():
    cur = db.cursor()
    query = """select name, value from admin_config_vtex"""
    cur.execute(query)
    data = cur.fetchall()
    return(json.dumps(data, indent=4))

    
    



