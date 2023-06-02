
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import time

img = Image.open()
imggray = img.convert('LA')
plt.figure(figsize=(9,6))
plt.imshow(imggray)

