'''
For more information about pymysql see http://zetcode.com/python/pymysql/
'''
import pymysql
import random
import string
import hashlib


host = "database"
user = "root"
pwd = "secure"
db_name = "myDatabase"

arrows = ">>>>>>>>>>>>>>>>>>>>"



try:
    # Establish database connection
    db = pymysql.connect(host, user, pwd, db_name)
    handler = db.cursor()
    # Commit changes to db as soon as a query has been executed
    db.autocommit(True)
except pymysql.InternalError as error:
    code, msg = error.args
    print(arrows, code, msg)



def get_item(item):
    try:
        handler.execute("SELECT * FROM items WHERE BINARY item_name=%s", item)
        handler.fetchall()
    except pymysql.InternalError as error:
        code, msg = error.args
        print(arrows, code, msg)

    if (handler.rowcount > 0):
        return True
    return False
