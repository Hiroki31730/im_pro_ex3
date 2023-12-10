#教科書P.103図5.5の加重平均化フィルタ（３ｘ３）および（５ｘ５）と、
# P.102図5.3の平均化フィルタ（３ｘ３）および（５ｘ５）を、任意の画像に適用し、
# それぞれのフィルタの効果を”比較検討”しなさい。

import cv2
import numpy as np
from matplotlib import pyplot as plt


#平均化フィルタ3*3のカーネル作成
kernel_1 = np.ones((3,3)) / 9
#平均化フィルタ5*5のカーネル作成
kernel_2 = np.ones((5,5)) / 25

#加重平均フィルタ3*3のカーネル作成
kernel_3 = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16
#加重平均フィルタ5*5のカーネル作成
kernel_4 = np.array([[1, 4, 6, 4, 1], 
                     [4, 16, 24, 16, 4], 
                     [6, 24, 36, 24, 6],
                     [4, 16, 24, 16, 4],
                     [1, 4, 6, 4, 1]]) / 256

#画像の読み込み
img = cv2.imread("im2.jpg")

#作成したカーネルを元画像に適用する
dst = cv2.filter2D(img, -1, kernel_1)
dst2 = cv2.filter2D(img, -1, kernel_2)
dst3 = cv2.filter2D(img, -1, kernel_3)
dst4 = cv2.filter2D(img, -1, kernel_4)

# 画像を表示
cv2.imshow("img",img)
cv2.imshow("img2",dst)
cv2.imshow("img3",dst2)
cv2.imshow("img4",dst3)
cv2.imshow("img5",dst4)
cv2.waitKey(0)
cv2.destroyAllWindows()

#ヒストグラムを表示
plt.hist(img.ravel(),256,[0,256], alpha=0.5)
plt.hist(dst.ravel(),256,[0,256], alpha=0.5)
plt.hist(dst2.ravel(),256,[0,256], alpha=0.5)
plt.hist(dst3.ravel(),256,[0,256], alpha=0.5)
plt.hist(dst4.ravel(),256,[0,256], alpha=0.5)
plt.show()