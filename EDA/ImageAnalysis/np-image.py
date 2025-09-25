import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import requests
from io import BytesIO

def get_image_from_url(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content)).convert("RGB")

peackock_url = 'https://m.media-amazon.com/images/I/81JSw5mE54L._UF894,1000_QL80_.jpg'
elephant_url = 'https://upload.wikimedia.org/wikipedia/commons/3/37/African_Bush_Elephant.jpg'

elephant = get_image_from_url(elephant_url)
#peacock = get_image_from_url(peackock_url)


#display image 

'''plt.figure(figsize=(10,10))
plt.imshow(elephant)
plt.title('Elephant')
plt.axis('off')
plt.show()'''

ele_array = np.array(elephant)
#print(ele_array.shape)

#display gray scale images 

color_ele = np.array(elephant)
elephant_gray = elephant.convert("L")
ele_grey = np.array(elephant_gray)
# Convert RGB to grayscale using luminosity method
#gray_ele = 0.2989 * color_ele[:, :, 0] + 0.5870 * color_ele[:, :, 1] + 0.1140 * color_ele[:, :, 2]

# Now display with inferno colormap
plt.imshow(ele_grey, cmap='magma')
plt.axis('off')
plt.title('Elephant with Inferno Colormap')
plt.show()

