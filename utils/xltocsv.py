import pandas as pd

def abc(s):
    if s==' ':
        return None
    i=0
    j=len(s)-1
    while s[i]==' ':
        i=i+1
    while s[j]==' ':
        j=j-1
    return s[i:j+1]

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

ing=pd.read_csv('ingredients.csv')
inglist=list(ing['name'].values)
#_id={}
#for obj in ingobj:
#    _id[obj['name']]=obj['_id']

check={}
check['dishtype']=dishtype
check['mealtype']=mealtype
check['ingredients']=inglist
check['mark']=mark

recipe_columns=[
        'title',
        'description',
        'instructions',
        'cuisine',
        'dishtype','mark','images','timetocook','mealtype'
        ]
recipe=pd.DataFrame(columns=recipe_columns)
ingredientUsed_columns=['id','quantity','directions','ingredient_name_id','recipe_name_id']
ingredientUsed=pd.DataFrame(columns=ingredientUsed_columns)

errors=0
q=0
for i in range(df.shape[0]):
    g={}
    j={}
    error=False
    for col in cols:
        if col=='image':
            map_obj=list(map(lambda x: abc(x),df[col].iloc[i].split(',')))
            urls="{"+'"'+map_obj[0]+'"'
            for url in map_obj[1:]:
                urls=urls+','+'"'+url+'"'
            urls=urls+"}"
            g['images']=urls
        elif col in risk:
            if pd.isna(df[col].iloc[i]):
                if col=='mark':
                    error=True
                    print(1)
                    
                else:
                    g[col]=''
            else:
                if (df[col].iloc[i] in check[col]) :
                    g[col]=df[col].iloc[i]
                else:
                    error=True
                    print(2,col,df[col].iloc[i])
        elif col=='timetocook':
            #print(df[col].iloc[i])
            time=df[col].iloc[i]
            hh=0
            mm=0
            if time.find('h')!=-1:
                hh=int(abc(time.split('h')[0]))
                if time.split('h')[-1].find('m')!=-1:
                    mm=int(abc(time.split('h')[-1].split('m')[0]))
            else:
                mm=int(abc(time.split('m')[0]))
            g[col]=str(hh)+':'+str(mm)+':'+'00'
        elif col =='ingredients':
            appendlist=[]
            for couple in df[col].iloc[i].split(';'):
                h={}
                arr=couple.split('-')
                if len(arr)!=2:
                    error=True
                    print(3,arr)
                    break
                h['quantity']=abc(arr[0])
                itemlist=arr[1].split(',')
                filter_object = filter(lambda x: x != "", itemlist)
                itemlist=list(filter_object)
                if itemlist[0] not in check['ingredients']:
                    error=True
                    print(4,itemlist[0])
                h['ingredient_name_id']=itemlist[0]
                h['directions']=''
                h['recipe_name_id']=df['title'].iloc[i]
                if len(itemlist)>1:
                    map_obj=map(lambda x: abc(x),itemlist[1:])
                    blank=''+list(map_obj)[0]
                    for dirs in list(map_obj)[1:]:
                       blank=blank+','+dirs
                    h['directions']=blank
                appendlist.append(h)
        else:
            g[col]=abc(df[col].iloc[i])
    if error:
        errors=errors+1
        print('error in row '+str(i+1))
    recipe.loc[i]=pd.Series(g)
    for ingre in appendlist:
        ingre['id']=q+1
        ingredientUsed.loc[q]=pd.Series(ingre)
        q=q+1
print('total errors='+str(errors))


if errors==0:
    recipe.to_excel('xl.xlsx',index=False)
    ingredientUsed.to_csv('ingredientUsed.csv',index=False,escapechar=';')




