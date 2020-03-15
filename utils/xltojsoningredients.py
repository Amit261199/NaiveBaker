# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 10:42:32 2020

@author: This-PC
"""
import json
import pandas as pd

ing=pd.read_excel('ingredients.xlsx')
cols=list(ing.columns)


jsonlist=[]
for i in range(ing.shape[0]):
    g={}
    for col in cols:
        g[col]=ing[col].iloc[i]
    
    jsonlist.append(g)
    
f=open('ingredients.json','w')
f.write('[\n')
string=json.dumps(jsonlist[0],indent=4)
f.write(string)
if len(jsonlist)>1:
    for obj in jsonlist[1:]:      
        string=json.dumps(obj,indent=4)
        f.write(',\n')
        f.write(string)
    
f.write(']')
        