# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector

# 数据库配置信息
db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'Lm151413',
    'database': 'lg_info',
    'charset': 'utf8'
}


class LgspiderPipeline(object):
    # 获取数据库连接和游标
    def __init__(self):
        self.connection = mysql.connector.connect(**db_config)
        self.cursor = self.connection.cursor()

    # Pipeline必须实现的方法，对收集好的item进行一系列处理
    def process_item(self, item, spider):
        # 存储"的SQL语句
        sql = "insert into info01(title, salary, position, time,company) values(%s, %s, %s, %s, %s)"
        paras = (item['title'], item['salary'],
                 item['position'], item['time'], item['company'])
        try:
            self.cursor.execute(sql, paras)

            self.connection.commit()
        except mysql.connector.Error as e:
            # 若存在异常则抛出
            print(e.args)
        return item
