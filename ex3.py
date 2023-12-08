#適当な１枚の画像を中心軸に関して左右反転させて表示せよ。
import cv2

#画像の読み込み
img = cv2.imread("im2.jpg")
#サイズの変更
img = cv2.resize(img, dsize=(700,400))

#画像の左右反転
re_img = cv2.flip(img,1)

# 画像を表示
cv2.imshow("img",img)  
cv2.imshow("re_img",re_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
