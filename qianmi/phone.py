# coding:utf-8
import os
import random
from NumberSection import *
from pymongo import MongoClient
import datetime

DC_PATH = "new.txt"


# 随机生成手机号码
def createPhone():
    prelist = p137
    return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(4))

def local_db():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.new
    collection = db.phone
    with open("new.txt",'r') as tp:
        a = tp.read()

    for i in a.split("\n"):
        post = {
                "text": "{}".format(i),
                "date": datetime.datetime.utcnow()
        }
        try:
            post_id = collection.insert_one(post)
        except:
            pass


if __name__ == '__main__':
    # while True:
    #     id = createPhone()
    #     with open(DC_PATH, 'r') as tp:
    #         phone = tp.read().split("\n")
    #     if id in phone:
    #         continue
    #     else:
    #         with open(DC_PATH, 'a') as tp:
    #             tp.write(id + "\n")

    local_db()
