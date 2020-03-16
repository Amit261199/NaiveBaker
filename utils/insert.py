# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 12:04:06 2020

@author: This-PC
"""

import json
from bson import objectid
from pymongo import MongoClient
client=MongoClient('mongodb+srv://AmitAgarwal:AmitAgarwal@amittaiwan-bk4uh.gcp.mongodb.net/test?authSource=admin&replicaSet=AmitTaiwan-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=true')
db=client.NaiveBaker
x=input('insert recipes or ingredients?')
if(x=='ingredients'):
    f=open('ingredients.json')
    ing=json.load(f)
    f.close()
    
    response=db.buildpantry_ingredient.insert_many(ing)
    
    print(len(response.inserted_ids))
elif(x=='recipes'):

    f=open('recipes.json')
    recipes=json.load(f)
    f.close()
    for recipe in recipes:
        for instr in recipe['ingredientdetails']:
            instr['ingredient']=objectid.ObjectId(instr['ingredient']['_id']['$oid'])
    response=db.buildpantry_recipe.insert_many(recipes)