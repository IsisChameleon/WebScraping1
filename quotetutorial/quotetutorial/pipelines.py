# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo


class QuotetutorialPipeline(object):

    def __init__(self):
        self.connection = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.connection["myquotes"]
        self.collection = db["tb_quotes"]

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item


# THIS PART IS IF YOU USE SQLITE
# import sqlite3
#
# class QuotetutorialPipeline(object):
#
#     def __init__(self):
#         self.create_connection()
#         self.create_table()
#
#     def create_connection(self):
#         self.conn = sqlite3.connect("myquotes.db")
#         self.curr = self.conn.cursor()
#
#     def create_table(self):
#         self.curr.execute("""drop table if exists tb_quotes""")
#         self.curr.execute("""create table tb_quotes (
#                                      title text,
#                                      author text,
#                                      tag text
#                                      )""")
#
#     def process_item(self, item, spider):
#         self.store_db(item)
#         return item
#
#     def store_db(self,item):
#         self.curr.execute("""insert into tb_quotes values (?,?,?)""",(
#              item['title'][0],
#              item['author'][0],
#              item['tag'][0]
#         ))
#         self.conn.commit()