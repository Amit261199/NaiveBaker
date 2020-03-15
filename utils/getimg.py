# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 19:30:55 2020

@author: This-PC
"""

import urllib3
from bs4 import BeautifulSoup

import pandas as pd
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

ing=pd.read_excel('ingredients.xlsx')
urls=[]
for i in range(ing.shape[0]):
    arr=ing['ingredients'].iloc[i].split(' ')
    Ingredient=arr[0]
    if(len(arr)>1):
        for word in arr[1:]:
            Ingredient=Ingredient+'+'+word
        
    url='https://www.google.com/search?tbm=isch&q='+Ingredient
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data,features='lxml')
    images=soup.findAll('img')
    urls.append(images[4]['src'])
    print(i)
    
ing['image']=urls

ing.to_excel('ingredients.xlsx',index=False)
