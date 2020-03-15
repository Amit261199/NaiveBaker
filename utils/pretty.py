import json

name='buildpantry_ingredient.json'
s=[]
with open(name,'r') as f:
    for line in f:
       s.append(json.dumps(json.loads(line),indent=4))
f=open(name,'w')
f.write('[\n')
for i in s:
    f.write(i)
    f.write(',\n')
f.write(']\n')
f.close()
        
    