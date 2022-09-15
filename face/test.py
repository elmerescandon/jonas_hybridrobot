import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('faces.jpg',0)
img = img[3:611,3:611]
print(img.shape)
# cv2.imshow('image', img)



img_matrix = np.zeros((76,76,64))
count = 0
for i in range(8):
    for j in range(8):
        img_matrix[:,:,count] = img[i*76:i*76+76,j*76:j*76+76]  
        count += 1

test_img = img_matrix[:,:,7] > 75

plt.imshow(img_matrix[:,:,7]>10,cmap='gray')
plt.show()

# Alegre, Triste, Molesto, Normal