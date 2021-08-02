import cv2 as cv
import numpy as np
A = np.zeros((240, 240))
A[240//3:(240)*2//3,:] = 255//2;
A[(240)*2//3:240,:] = 255;
cv.imwrite("BGW.png",A)

B = np.zeros((240, 240, 3));
S = np.array(np.shape(B))
print(S)
for i in range(S[0]//2):
    for j in range (i):
        B[i][j][:] = 255;
        B[i][j][:] = 255;
for i in range (S[0]//2, S[0]):
    for j in range(S[0]- i):
        B[i][j][:] = 255;
        B[i][j][:] = 255;

for i in range(S[1]//2):
    for j in range(i):
        B[j][i][1] = 255;
for i in range (S[1]//2, S[1]):
    for j in range(S[1]- i):
        B[j][i][1] = 255;
        
for i in range(S[0]-1,S[0]//2, -1):
    for j in range(i,S[0]//2,-1):
         B[j][i][0] = 255;
for i in range(S[0]//2, 0, -1):
    for j in range(S[0]-1,S[0]-i, -1):
        B[i][j][0] = 255;


for i in range(S[0]//2,S[0]-1, 1):
    for j in range(i,S[0]//2,-1):
        B[i][j][2] = 255;
for i in range (S[0]//2, 0, -1):
    for j in range(S[0]-1,S[0]-i, -1):
        B[j][i][2] = 255;

                

        
cv.imwrite("CMYK.jpg",B)
