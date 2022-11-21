#Bibliotecas
import cv2

#abrir imagen
img = cv2.imread('libro.jpg',0)
#Aplicar Canny
bordeCanny = cv2.Canny(img,100,200)
#Mostrar imágenes
cv2.imshow('Original', img)
cv2.imshow('Canny', bordeCanny)
#Presionar una tecla para dejar de ejecutar
cv2.waitKey(0)
cv2.destroyAllWindows()
