import matplotlib.pyplot as plt
import os.path
import PIL.imagedraw
import PIL
from PIL import image

directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'trump.jpg')
img = plt.imread(filename)

fig, ax = plt.subplots(1, 1) 
ax.imshow(img, interpolation='none')
fig.show()

def trump():
