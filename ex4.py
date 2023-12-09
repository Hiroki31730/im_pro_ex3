#適当な１枚の画像を３ｘ３のモザイクタイル状に区切って、各タイルを順番に、もしくはランダムに選んで５秒毎に左右反転させてみよ。

import cv2
import numpy as np
import glob

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

#分割した画像と反転した画像をディレクトリex4下に保存する
for i, j in enumerate(np_ar):
    save_path = f"ex4/split{i:02d}.png"
    inversion = cv2.flip(j,1)
    save_path2 = f"ex4/split2{i:02d}.png"
    cv2.imwrite(str(save_path), j)
    cv2.imwrite(str(save_path2), inversion)

#元の画像の表示
cv2.imshow("origin", img)
cv2.waitKey(5000)
  
#分割、反転した画像を表示する
for x in range(0,9):
    img = cv2.imread(f"ex4/split{x:02d}.png")
    re_img = cv2.flip(img,1)   
    re_img = cv2.resize(re_img, dsize=(700,400))
    cv2.imshow("img",re_img)
    cv2.waitKey(5000)

#分割、反転した画像を結合する
img1 = cv2.imread("ex4/split200.png")
img2 = cv2.imread("ex4/split201.png")
img3 = cv2.imread("ex4/split202.png")
img4 = cv2.imread("ex4/split203.png")
img5 = cv2.imread("ex4/split204.png")
img6 = cv2.imread("ex4/split205.png")
img7 = cv2.imread("ex4/split206.png")
img8 = cv2.imread("ex4/split207.png")
img9 = cv2.imread("ex4/split208.png")

#変数に保存した画像を横に結合する
beside1 = cv2.hconcat((img1, img2, img3))
beside2 = cv2.hconcat((img4, img5, img6))
beside3 = cv2.hconcat((img7, img8, img9))

#横に結合した画像を縦に結合する
vertical = cv2.vconcat((beside1, beside2, beside3))

#反転し、結合した画像を表示する。
cv2.imshow('ex', vertical)
cv2.waitKey(0)



cv2.destroyAllWindows()