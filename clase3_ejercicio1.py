import numpy as np
import pandas as pd
import cv2

arr = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print (arr.shape)#2D ESCLA DE GRISES Y 3D ES A COLORES RGB 
print(arr.dtype)
data = ["imagen1.jpg, image2.jpg, image3.jpg"]
data_dict = {"filename": data, 
             "white": [640, 800, 1024],
             "height": [480,600, 780],}
df = pd.DataFrame(data)
print(df)

#clase4 ejercicio1
