import cv2
import numpy as np
path = "/content/drive/MyDrive/Colab Notebooks/leena.png"
img = np.zeros((300,300,3))
img[0:149,0:149,2] = 256
img[150:299,0:149,0] = 256
img[0:149,149:299,1] = 256
img[150:299,149:299,:] = 256
cv2.imwrite(path+"first.png",img)
