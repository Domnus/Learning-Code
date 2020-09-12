import cv2

imagem = cv2.imread(
    '/home/bentocarlos/Learning-Code/College/Machine Learning/Aula 4/pessoas.jpg')
print(imagem)

classificador = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

imagemcinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

deteccoes = classificador.detectMultiScale(imagemcinza)
