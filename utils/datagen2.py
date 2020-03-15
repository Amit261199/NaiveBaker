import pandas as pd

ing=pd.read_excel('ingredients.xlsx')
inglist=list(ing['name'].values)
categories=list(set(list(ing['category'].values)))
category={}
for i in range(ing.shape[0]):
    category[ing['name'].iloc[i]]=ing['category'].iloc[i]
            
            
df=pd.read_excel('recipes_f.xlsx')
for i in range(25,min(df.shape[0],50)):
    s=df['ingredients'].iloc[i]
    lists=s.split(';')
    for k in range(len(lists)):
        x=-1
        result={}
        while(x==-1):
            print(i,lists[k])
            substr=input('type substring to search--enter 00 to skip\n')
            if substr=='00':
                break
            t=0
            for j in range(len(inglist)):
                if inglist[j].find(substr)!=-1:
                    result[t]=inglist[j]
                    t=t+1
            print(result)
            x=int(input('please select an ingredient:select -1 to re-search and -2 to add a new ingredient to the list\n'))
        if x==-1:
            continue
        if x==-2:
            empty=input('enter the ingredient name')
            inglist.append(empty)
            print(categories)
            cat=input('select category')
            category[empty]=cat
        else:
            empty=result[x]
        y=int(input('Want to enter after comma result(0 or 1)?\n'))
        if y==0:
            for string in lists[k].split('-')[1].split(',')[1:]:
                empty=empty+','+string
        else:
            empty=empty+','+input('please enter\n')
        lists[k]=lists[k].split('-')[0]+'-'+empty
    
    amit=lists[0]
    if len(lists)>1:
        for st in lists[1:]:
            amit=amit+';'+st
    df['ingredients'].iloc[i]=amit
    df.to_excel('recipes_f.xlsx',index=False)

catlist=[]
for ingredient in inglist:
    catlist.append(category[ingredient])

dictionary={'ingredients':inglist,'category':catlist}
ingredients=pd.DataFrame.from_dict(dictionary)
ingredients.to_excel('ingredients.xlsx',index=False)