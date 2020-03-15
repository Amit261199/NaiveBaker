

import pandas as pd
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt


ing=pd.read_excel('ingredients.xlsx')

for i in range(685,ing.shape[0]):
    print(ing['ingredients'].iloc[i])
    response = requests.get(ing['image'].iloc[i])
    img = Image.open(BytesIO(response.content))
    plt.imshow(img)
    plt.show()
    x=input('press enter to proceed\n')
    
    


