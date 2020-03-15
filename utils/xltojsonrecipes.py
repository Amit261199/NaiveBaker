import pandas as pd
import json

f=open('buildpantry_ingredient.json')
ingobj=json.load(f)
f.close()
    

def abc(s):
    i=0
    j=len(s)-1
    while s[i]==' ':
        i=i+1
    while s[j]==' ':
        j=j-1
    return s[i:j+1]


def imgdict(x):
    j={}
    j['url']=x
    return j

df=pd.read_excel('recipes.xlsx')
cols=list(df.columns)
risk=['dishtype','mealtype','mark']
dishtype=[
        'Appetizers & Snacks',
'Bread Recipes',
'Cake Recipes',
'Candy and Fudge',
'Casserole Recipes',
'Christmas Cookies',
'Cocktail Recipes',
'Cookie Recipes',
'Mac and Cheese Recipes',
'Main Dish',
'Pasta Salad Recipes',
'Pasta Recipes',
'Pie Recipes',
'Pizza',
'Sandwiches',
'Sauces and Condiments',
'Smoothie Recipes',
'Soups, Stews, and Chili',
'Side Dish',
'Salad'
        ]
mark=[
      'green','red','yellow'
      ]

mealtype=[
        'Breakfast and Brunch',
'Desserts',
'Dinners',
'Lunch',
        ]

ing=pd.read_excel('ingredients.xlsx')
inglist=list(ing['name'].values)
_id={}
for obj in ingobj:
    _id[obj['name']]=obj

check={}
check['dishtype']=dishtype
check['mealtype']=mealtype
check['ingredients']=inglist
check['mark']=mark
df.fillna('NA',inplace=True)
errors=0


jsonlist=[]
for i in range(df.shape[0]):
    g={}
    error=False
    for col in cols:
        if col=='image':
            map_obj=map(lambda x: imgdict(abc(x)),df[col].iloc[i].split(','))
            g[col]=list(map_obj)
        elif col in risk:
            if df[col].iloc[i]=='NA':
                if col=='mark':
                    error=True
                    print(1)
            else:
                if (df[col].iloc[i] in check[col]) :
                    g[col]=df[col].iloc[i]
                else:
                    error=True
                    print(2,col,df[col].iloc[i])
        elif col =='ingredients':
            ingredients_list=[]
            for couple in df[col].iloc[i].split(';'):
                h={}
                arr=couple.split('-')
                if len(arr)!=2:
                    error=True
                    print(3,arr)
                    break
                qty=arr[0]
                h['quantity']=abc(qty)
                itemlist=arr[1].split(',')
                filter_object = filter(lambda x: x != "", itemlist)
                itemlist=list(filter_object)
                if itemlist[0] not in check['ingredients']:
                    error=True
                    print(4,itemlist[0])
                h['ingredient']=_id[itemlist[0]]
                if len(itemlist)>1:
                    map_obj=map(lambda x: abc(x),itemlist[1:])
                    h['directions']=list(map_obj)
                ingredients_list.append(h)
            g['ingredientdetails']=ingredients_list
        else:
            g[col]=abc(df[col].iloc[i])
        
    if error:
        errors=errors+1
        print('error in row '+str(i+1))
    jsonlist.append(g)

print('total errors='+str(errors))


if errors==0:
    f=open('recipes.json','w')
    f.write('[\n')
    string=json.dumps(jsonlist[0],indent=4)
    f.write(string)
    if len(jsonlist)>1:
        for obj in jsonlist[1:]:      
            string=json.dumps(obj,indent=4)
            f.write(',\n')
            f.write(string)
        
    f.write(']')




