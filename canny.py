#Bibliotecas
import cv2

capture = cv2.VideoCapture(0)
while (capture.isOpened()):
	ret, frame = capture.read()
	if (ret == True):
		#Aplicar Canny
		bordeCanny = cv2.Canny(frame,100,200)
		#Mostrar imágenes
		cv2.imshow('Original', frame)
		cv2.imshow('Canny', bordeCanny)
		#Presionar una tecla para dejar de ejecutar
		if (cv2.waitKey(1) == ord('s')):
			break
	else:
		break
capture.release()
cv2.destroyAllWindows()
