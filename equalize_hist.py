import cv2

img = cv2.imread("donkey.png", 0)
eq = cv2.equalizeHist(img)
cv2.imshow('image1',img)
cv2.imshow('image2',eq)
cv2.waitKey(0)
cv2.destroyAllWindows()
