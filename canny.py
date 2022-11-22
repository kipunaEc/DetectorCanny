import cv2

img = cv2.imread('libro.jpg',0)
bordeCanny = cv2.Canny(img,10,50)

cv2.imshow('Original', img)
cv2.imshow('blur', bordeCanny)

cv2.waitKey(0)
cv2.destroyAllWindows()
