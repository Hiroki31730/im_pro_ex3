#図4.21 と 図4.22のようなαブレンディングを実行するプログラムをそれぞれ作成し、作成したプログラムを適当なカラー画像2枚に適用し正しく実行されていることを確認しなさい。

import cv2

#画像の読み込み
pic1 = cv2.imread("ex2-1.jpg")
pic2 = cv2.imread("ex2-2.jpg")

#画像のサイズを統一
pic1 = cv2.resize(pic1, dsize=(600,400))
pic2 = cv2.resize(pic2, dsize=(600,400))

#アルファ値の設定
alpha = 0.6
#アルファブレンディングを実行する関数
pic3 = cv2.addWeighted(pic1, alpha, pic2, 1 - alpha, 0)

# 画像を表示
cv2.imshow("pic1",pic1)  
cv2.imshow("pic2",pic2)
cv2.imshow("pic3", pic3)
cv2.waitKey(0)
cv2.destroyAllWindows()