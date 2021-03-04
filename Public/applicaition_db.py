# coding=utf-8
import cx_Oracle,pymysql
import re,time


def votesrv_bizdev(sql):
    """
    基础服务库BIZDEV
    "votesrvuser/votesrvuser@10.10.11.82:1521/BIZDEV"
    """
    db = cx_Oracle.connect("votesrvuser/votesrvuser@10.10.11.82:1521/BIZDEV")
    cr = db.cursor()
    try:
        cr.execute(sql)
        if re.search('SELECT',sql[0:6],re.I):
            return cr.fetchall()
    finally:
        db.commit()
        cr.close()
        db.close()


def infob_bizdev(sql):
    """采编系统库BIZDEV
    "infob/infob@10.10.11.82:1521/BIZDEV"
    """
    db = cx_Oracle.connect("infob/infob@10.10.11.82:1521/BIZDEV")
    cr = db.cursor()
    try:
        cr.execute(sql)
        if re.search('SELECT',sql[0:6],re.I):
            return cr.fetchall()
    finally:
        db.commit()
        cr.close()
        db.close()


def sseSivsDB(sql,timeout=5):
    """投票统计自动化系统本地库"""
    db = pymysql.connect(
        host='10.10.11.197',
        port=3306,
        user='sivsmgr',
        passwd='sivsmgr',
        db='SSE_SIVS_DB',
        charset='utf8'
    )
    cr = db.cursor()
    try:
        cr.execute(sql)
        data = cr.fetchall()
        if data !=():
            if re.search('SELECT', sql[0:6], re.I):
                return data
            times=0
            while data==():
                time.sleep(1)
                times += 1
                print("尝试第%d次链接数据库"%times)
                data_1 = cr.fetchall()
                if data_1!=():
                    if re.search('SELECT', sql[0:6], re.I):
                        return data_1
                if times == timeout:
                    print("已超时，未查询到数据：",cr.fetchall())
                    break
    finally:
        db.commit()
        cr.close()
        db.close()


nt=time.strftime("%Y/%m/%d")