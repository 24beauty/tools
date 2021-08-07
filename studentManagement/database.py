import pymysql


def run_query(query):
    db = pymysql.connect(host="localhost", user="root", password="root", db="sys", charset="utf8")
    cursor = db.cursor()
    try:
        cursor.execute(query)
        db.commit()
    except():
        db.rollback()
    db.close()


def run_query_executemany(query, data):
    db = pymysql.connect(host="localhost", user="root", password="root", db="sys", charset="utf8")
    cursor = db.cursor()
    try:
        cursor.executemany(query, data)
        db.commit()
    except():
        db.rollback()
    db.close()
