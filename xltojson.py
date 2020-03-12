import pandas as pd

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
inglist=list(ing['ingredients'].values)

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
            g[col]=df[col].iloc[i].split(',')
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
                h['quantity']=qty
                itemlist=arr[1].split(',')
                filter_object = filter(lambda x: x != "", itemlist)
                itemlist=list(filter_object)
                if itemlist[0] not in check['ingredients']:
                    error=True
                    print(4,itemlist[0])
                h['ingredient']=itemlist[0]
                if len(itemlist)>1:
                    h['directions']=itemlist[1:]
                ingredients_list.append(h)
            g[col]=ingredients_list
        else:
            g[col]=df[col].iloc[i]
        
    if error:
        errors=errors+1
        print('error in row '+str(i+1))
    jsonlist.append(g)

print('total errors='+str(errors))


 

