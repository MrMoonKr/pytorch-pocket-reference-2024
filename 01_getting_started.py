

import torch

print( torch.__version__ )
print( torch.cuda.is_available() )


import urllib.request

url = 'https://upload.wikimedia.org/wikipedia/commons/4/45/A_small_cup_of_coffee.JPG'
fpath = 'coffee.jpg'
urllib.request.urlretrieve( url, fpath )


import matplotlib.pyplot as plt
from PIL import Image

img = Image.open('coffee.jpg')
plt.imshow( img )

print( "just for break point to see the image" )