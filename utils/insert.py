# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 12:04:06 2020

@author: This-PC
"""

import json
f=open('ingredients.json')
ing=json.load(f)
f.close()

from pymongo import MongoClient

client=MongoClient('mongodb+srv://AmitAgarwal:AmitAgarwal@amittaiwan-bk4uh.gcp.mongodb.net/test?authSource=admin&replicaSet=AmitTaiwan-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=true')
db=client.NaiveBaker


response=db.buildpantry_ingredient.insert_many(ing)

print(len(response.inserted_ids))
