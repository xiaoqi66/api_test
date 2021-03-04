# coding=utf-8
import cx_Oracle,pymysql
import re,sys,os
os.environ['NLS_LANG']='SIMPLIFIED CHINESE_CHINA.UTF8'


def getOracleBizdevData(conf,sql):
    db = cx_Oracle.connect(conf)
    cr = db.cursor()
    try:
        if re.search("SELECT",sql,re.I):
            cr.execute(sql)
            return cr.fetchall()
        elif re.search("UPDATE",sql,re.I):
            cr.execute(sql)
        elif re.search("DELETE",sql,re.I):
            cr.execute(sql)
        elif re.search("INSERT",sql,re.I):
            cr.execute(sql)
        else:
            return False
    finally:
        db.commit()
        cr.close()
        db.close()


def getMysqlSseautotestData(sql):
        db = pymysql.connect(host='10.10.11.197',port=3306,
                             user='sseautotest',passwd='sseautotest',db='sse_auto_test',charset='utf8')
        cr = db.cursor()
        try:
            if re.search("SELECT",sql,re.I):
                cr.execute(sql)
                return cr.fetchall()
            elif re.search("UPDATE",sql,re.I):
                cr.execute(sql)
            elif re.search("DELETE",sql,re.I):
                cr.execute(sql)
            elif re.search("INSERT",sql,re.I):
                cr.execute(sql)
            else:
                return False
        finally:
            db.commit()
            cr.close()
            db.close()

# print  u"Oracle数据：",getOracleBizdevData("SELECT * FROM GDDH_BASIC_INFO")[0]
# print  u"Oracle数据：",getOracleBizdevData("SELECT * FROM GDDH_BASIC_INFO")[0][7]
# print u"Mysql数据：",getMysqlSseautotestData("select * from test_for_interface")[0]
# print u"Mysql数据：",getMysqlSseautotestData("select * from test_for_interface")[0][-1]