#教科書P.123-124の可変鮮鋭化フィルタを任意の画像に適用し、その効果を調べなさい。

import cv2
import numpy as np
from matplotlib import pyplot as plt

#先鋭化を行うカーネルの関数を作成
def sharp_k(k: int):
    return np.array([
                [-k / 9, -k / 9, -k / 9],
                [-k / 9, 1 + 8 * k / 9, k / 9],
                [-k / 9, -k / 9, -k / 9]
                ], np.float32)

#画像の読み込み、サイズの変更
img = cv2.imread("im2.jpg")
img = cv2.resize(img, dsize=(700,400))

#カーネルの作成
kernel = sharp_k(3)

#カーネルを任意の画像に適用
dst = cv2.filter2D(img, -1, kernel).astype("uint8")

#画像の表示
cv2.imshow("origin", img)
cv2.imshow("img",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

#ヒストグラムを表示
plt.hist(img.ravel(),256,[0,256], alpha=0.5)
plt.hist(dst.ravel(),256,[0,256], alpha=0.5)

plt.show()
