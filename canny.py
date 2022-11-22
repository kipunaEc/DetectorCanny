#Bibliotecas
import cv2

#Capturar información de la webCam
capture = cv2.VideoCapture(0)
while (capture.isOpened()):
	ret, frame = capture.read()
	if (ret == True):
		#Aplicar Canny
		bordeCanny = cv2.Canny(frame,10,50)
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
