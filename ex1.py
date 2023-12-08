#教科書P.85　式(4.2)で表されるトーンカーブ変換（γ変換）を実行するプログラムを作成しなさい。

import cv2
import numpy as np

#任意の画像の読み込み
img =cv2.imread("im2.jpg")
#画像が小さいのでサイズ変更
img = cv2.resize(img, dsize=(700,400))

#ガンマ値を指定
gamma = 1.5
#ガンマ変換の初期値
Gimg= np.zeros((256,1), dtype=np.uint8)

#式を適用
for i in range(256):
    Gimg[i][0] = 255 * (float(i)/255) ** (1.0 /gamma)

# 読込画像をガンマ変換
gamma_img = cv2.LUT(img,Gimg)

# 画像を表示
cv2.imshow("img",img)  
cv2.imshow("gamma",gamma_img)
cv2.waitKey(0)
cv2.destroyAllWindows()