#任意の画像から輪郭を抽出しなさい。できるだけ綺麗な輪郭を抽出すること。

import cv2

#画像の読み込み
img = cv2.imread("Fuji.jpg")

#オリジナル画像の表示
cv2.imshow("origin", img)
cv2.waitKey(0)


#画像をグレースケールに変換
gray_im = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 画像の白黒2値化
ret, dst = cv2.threshold(gray_im, 160, 255, cv2.THRESH_BINARY)

# 輪郭を抽出する
contours, hierarchy = cv2.findContours(dst, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 輪郭を画像に書き込む
output = cv2.drawContours(img, contours, -1, (0,255,0), 3)

#画像を表示
cv2.imshow("gray", gray_im)
cv2.imshow("BlackorWhite", dst)
cv2.imshow("last", output)
cv2.waitKey(0)
cv2.destroyAllWindows()