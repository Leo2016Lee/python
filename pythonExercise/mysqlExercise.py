# -*- coding: utf-8 -*-

import mysql.connector
import time


try:
    # 配置信息
    config = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'Lm151413',
        'database': 'historical_alarm_record',
        'charset': 'utf8'
    }
    #     连接数据库
    # con=mysql.connector.connect(host='localhost',port=3306,user='root',
    #                         password='root',database='test',charset='utf8')
    con = mysql.connector.connect(**config)
    print(con.connection_id)
    cursor1 = con.cursor()
    cursor1.execute("select * from alarmrecord")
    data = cursor1.fetchall()
    for row in data:
        fID = row[0]
        fVar = row[1]
        fDateTime = row[7]
        # 打印结果
        print("AlarmID=%i,AlarmVar=%s,AlarmDateTime=%s" %
              (fID, fVar, fDateTime))
    time.sleep(5)
    # 断开
    con.close()
except mysql.connector.Error as e:
    print(e.msg)
