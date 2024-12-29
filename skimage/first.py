import skimage as ski 
import matplotlib.pyplot as plt
import numpy as np
camera = ski.data.camera()
# print(type(camera))
coins=ski.data.coins()
threshold = ski.filters.threshold_otsu(coins)
# print(threshold)
# print(coins)
# print(coins.shape)
# print(ski.data.eagle())
eagle = ski.data.eagle()
plt.figure()
plt.imshow(eagle)
plt.show()
