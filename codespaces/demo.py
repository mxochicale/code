
# https://blog.shibayan.jp/entry/20220309/1646754054

import cv2
print(cv2.__version__)

source_image = cv2.imread('shibayan.png')
gray_image = cv2.cvtColor(source_image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('output.png', gray_image)