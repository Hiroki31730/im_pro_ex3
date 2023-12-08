#適当な１枚の画像を３ｘ３のモザイクタイル状に区切って、各タイルを順番に、もしくはランダムに選んで５秒毎に左右反転させてみよ。

import cv2
import numpy as np

#画像の読み込み
img = cv2.imread("im2.jpg")
#サイズの変更
img = cv2.resize(img, dsize=(700,400))

#行数
row = 3
#列数
col = 3

#画像を3*3で9分割する
np_ar = []
for row_img in np.array_split(img, row, axis=0):
    for col_img in np.array_split(row_img, col, axis=1):
        np_ar.append(col_img)

#分割した画像をディレクトリex4下に保存する
for i, j in enumerate(np_ar):
    save_path = f"ex4/split{i:02d}.png"
    cv2.imwrite(str(save_path), j)

#元の画像の表示
cv2.imshow("origin", img)
cv2.waitKey(5000)
    
#分割した画像を表示する
for x in range(0,9):
    img = cv2.imread(f"ex4/split{x:02d}.png")
    re_img = cv2.flip(img,1)
    re_img = cv2.resize(re_img, dsize=(700,400))
    cv2.imshow("img",re_img)
    cv2.waitKey(5000)

cv2.destroyAllWindows()
