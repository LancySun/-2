#!/usr/bin/python
# coding=utf-8

import datetime
from flask import Flask, render_template
#import pymysql
from MysqlHelper import MysqlHelper

app = Flask(__name__)
app.config.from_object('config')
app.debug = True


@app.route('/')
def hello_world():

    return render_template('index.html')


@app.route('/chartjs')
def chartjs():
    data1 = []
    data2 = []
    mh = MysqlHelper('localhost', 'root', 'wykl0920', 'test1', 'utf8')
    labels1 = ['ARTIK305S', 'ARTIK530', 'ARTIK710S', 'ARTIK710', 'ARTIK053', 'ARTIK055S', 'ARTIK530S', 'ARTIK533S']
    #for i in labels1:
     #   sql = "select SUM(testcases_pass_count) from test0 where starttime LIKE '2018-07-28%' and TARGET_MODEL=%s"
      #  data = mh.find(sql, repr(i))
       # print(data)
        #data2 = list(data)
        #if data2 == [None]:
         #   data2 = ['0']
        #print(data2)
        #data1.append(data[0])
    t='2018-07-20%'
    sql = "select SUM(testcases_pass_count) from test0 where starttime LIKE %s and TARGET_MODEL='ARTIK305S'"
    data1_1 = list(mh.find(sql,t))
    if data1_1 == [None]:
        data1_1 = ['0']
    data1.append(data1_1[0])
    sql = "select SUM(testcases_pass_count) from test0 where starttime LIKE %s and TARGET_MODEL='ARTIK530'"
    data1_2 = list(mh.find(sql,t))
    if data1_2 == [None]:
        data1_2 = ['0']
    data1.append(data1_2[0])
    sql = "select SUM(testcases_pass_count) from test0 where starttime LIKE %s and TARGET_MODEL='ARTIK710S'"
    data1_3 = list(mh.find(sql,t))
    if data1_3 == [None]:
        data1_3 = ['0']
    data1.append(data1_3[0])
    sql = "select SUM(testcases_pass_count) from test0 where starttime LIKE %s and TARGET_MODEL='ARTIK710'"
    data1_4 = list(mh.find(sql,t))
    if data1_4 == [None]:
        data1_4 = ['0']
    data1.append(data1_4[0])
    sql = "select SUM(testcases_pass_count) from test0 where starttime LIKE %s and TARGET_MODEL='ARTIK053'"
    data1_5 = list(mh.find(sql,t))
    if data1_5 == [None]:
        data1_5 = ['0']
    data1.append(data1_5[0])
    sql = "select SUM(testcases_pass_count) from test0 where starttime LIKE %s and TARGET_MODEL='ARTIK055S'"
    data1_6 = list(mh.find(sql, t))
    if data1_6 == [None]:
        data1_6 = ['0']
    data1.append(data1_6[0])
    sql = "select SUM(testcases_pass_count) from test0 where starttime LIKE %s and TARGET_MODEL='ARTIK530S'"
    data1_7 = list(mh.find(sql, t))
    if data1_7 == [None]:
        data1_7 = ['0']
    data1.append(data1_7[0])
    sql = "select SUM(testcases_pass_count) from test0 where starttime LIKE %s and TARGET_MODEL='ARTIK533S'"
    data1_8 = list(mh.find(sql, t))
    if data1_8 == [None]:
        data1_8 = ['0']
    data1.append(data1_8[0])
    sql = "select SUM(testcases_fail_count) from test0 where starttime LIKE %s and TARGET_MODEL='ARTIK305S'"
    data2_1 = list(mh.find(sql, t))
    if data2_1 == [None]:
        data2_1 = ['0']
    data2.append(data2_1[0])
    sql = "select SUM(testcases_fail_count) from test0 where starttime LIKE %s and TARGET_MODEL='ARTIK530'"
    data2_2 = list(mh.find(sql, t))
    if data2_2 == [None]:
        data2_2 = ['0']
    data2.append(data2_2[0])
    sql = "select SUM(testcases_fail_count) from test0 where starttime LIKE %s and TARGET_MODEL='ARTIK710S'"
    data2_3 = list(mh.find(sql, t))
    if data2_3 == [None]:
        data2_3 = ['0']
    data2.append(data2_3[0])
    sql = "select SUM(testcases_fail_count) from test0 where starttime LIKE %s and TARGET_MODEL='ARTIK710'"
    data2_4 = list(mh.find(sql, t))
    if data2_4 == [None]:
        data2_4 = ['0']
    data2.append(data2_4[0])
    sql = "select SUM(testcases_fail_count) from test0 where starttime LIKE %s and TARGET_MODEL='ARTIK053'"
    data2_5 = list(mh.find(sql, t))
    if data2_5 == [None]:
        data2_5 = ['0']
    data2.append(data2_5[0])
    sql = "select SUM(testcases_fail_count) from test0 where starttime LIKE %s and TARGET_MODEL='ARTIK055S'"
    data2_6 = list(mh.find(sql, t))
    if data2_6 == [None]:
        data2_6 = ['0']
    data2.append(data2_6[0])
    sql = "select SUM(testcases_fail_count) from test0 where starttime LIKE %s and TARGET_MODEL='ARTIK530S'"
    data2_7 = list(mh.find(sql, t))
    if data2_7 == [None]:
        data2_7 = ['0']
    data2.append(data2_7[0])
    sql = "select SUM(testcases_fail_count) from test0 where starttime LIKE %s and TARGET_MODEL='ARTIK533S'"
    data2_8 = list(mh.find(sql, t))
    if data2_8 == [None]:
        data2_8 = ['0']
    data2.append(data2_8[0])
    return render_template('./pages/charts/chartjs.html', data1=data1,data2=data2,labels1=labels1)


@app.route('/morris')
def morris():
    return render_template('./pages/charts/morris.html')


@app.route('/A710S')
def A710S():
    return render_template('./pages/charts/A710S.html')


@app.route('/flot')
def flot():
    return render_template('./pages/charts/flot.html')


@app.route('/inline')
def inline():
    return render_template('./pages/charts/inline.html')


@app.route('/Eagleye530')
def Eagleye530():
    return render_template('./pages/charts/Eagleye530.html')


@app.route('/ci')
def ci():
    today1 = datetime.date.today()
    print(today1)
    data11 = []
    data12 = []
    data13 = []
    data14 = []
    data15 = []
    data16 = []
    data17 = []
    data18 = []
    labels2 = []
    for i in range(1, 30):
        d = today1 - datetime.timedelta(days=i)
        d1 = str(d) + '%'
        labels2.append(d)
        mh = MysqlHelper('localhost', 'root', 'wykl0920', 'test1', 'utf8')
        sql = "SELECT sum(testcases_fail_count)+sum(testcases_pass_count) from (SELECT * FROM test0 where DATE_SUB(CURDATE(), INTERVAL 30 DAY) <= date(starttime)) test where starttime like %s and TARGET_MODEL = 'ARTIK305S'"
        data1 = mh.find(sql, d1)
        if data1 == (None,):
            data1 = ('0',)
        data2 = list(data1)
        print(data2[0])
        data11.append(data2[0])
        print(data11)
        sql = "SELECT sum(testcases_fail_count)+sum(testcases_pass_count) from (SELECT * FROM test0 where DATE_SUB(CURDATE(), INTERVAL 30 DAY) <= date(starttime)) test where starttime like %s and TARGET_MODEL = 'ARTIK530'"
        data1_1 = mh.find(sql, d1)
        if data1_1 == (None,):
            data1_1 = ('0',)
        data2_1 = list(data1_1)
        print(data2_1[0])
        data12.append(data2_1[0])
        print(data12)
        sql = "SELECT sum(testcases_fail_count)+sum(testcases_pass_count) from (SELECT * FROM test0 where DATE_SUB(CURDATE(), INTERVAL 30 DAY) <= date(starttime)) test where starttime like %s and TARGET_MODEL = 'ARTIK710S'"
        data1_2 = mh.find(sql, d1)
        if data1_2 == (None,):
            data1_2 = ('0',)
        data2_2 = list(data1_2)
        print(data2_2[0])
        data13.append(data2_2[0])
        print(data13)
        sql = "SELECT sum(testcases_fail_count)+sum(testcases_pass_count) from (SELECT * FROM test0 where DATE_SUB(CURDATE(), INTERVAL 30 DAY) <= date(starttime)) test where starttime like %s and TARGET_MODEL = 'ARTIK710'"
        data1_3 = mh.find(sql, d1)
        if data1_3 == (None,):
            data1_3 = ('0',)
        data2_3 = list(data1_3)
        data14.append(data2_3[0])
        sql = "SELECT sum(testcases_fail_count)+sum(testcases_pass_count) from (SELECT * FROM test0 where DATE_SUB(CURDATE(), INTERVAL 30 DAY) <= date(starttime)) test where starttime like %s and TARGET_MODEL = 'ARTIK053'"
        data1_4 = mh.find(sql, d1)
        if data1_4 == (None,):
            data1_4 = ('0',)
        data2_4 = list(data1_4)
        data15.append(data2_4[0])
        sql = "SELECT sum(testcases_fail_count)+sum(testcases_pass_count) from (SELECT * FROM test0 where DATE_SUB(CURDATE(), INTERVAL 30 DAY) <= date(starttime)) test where starttime like %s and TARGET_MODEL = 'ARTIK055S'"
        data1_5 = mh.find(sql, d1)
        if data1_5 == (None,):
            data1_5 = ('0',)
        data2_5 = list(data1_5)
        data16.append(data2_5[0])
        sql = "SELECT sum(testcases_fail_count)+sum(testcases_pass_count) from (SELECT * FROM test0 where DATE_SUB(CURDATE(), INTERVAL 30 DAY) <= date(starttime)) test where starttime like %s and TARGET_MODEL = 'ARTIK530S'"
        data1_6 = mh.find(sql, d1)
        if data1_6 == (None,):
            data1_6 = ('0',)
        data2_6 = list(data1_6)
        data17.append(data2_6[0])
        sql = "SELECT sum(testcases_fail_count)+sum(testcases_pass_count) from (SELECT * FROM test0 where DATE_SUB(CURDATE(), INTERVAL 30 DAY) <= date(starttime)) test where starttime like %s and TARGET_MODEL = 'ARTIK533S'"
        data1_7 = mh.find(sql, d1)
        if data1_7 == (None,):
            data1_7 = ('0',)
        data2_7 = list(data1_7)
        data18.append(data2_7[0])
    return render_template('./pages/CI overview/ci.html',data11=data11,data12=data12,data13=data13,data14=data14,data15=data15,data16=data16,data17=data17,data18=data18,labels2=labels2)


@app.route('/another')
def another():
    return render_template('./pages/Another Link/another.html')


if __name__ == "__main__":
    app.run(host='127.0.0.1')
