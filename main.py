import cv2

image = cv2.imread('humano.jpg')

cv2.imshow('Humano', image)
print(image)

casc = cv2.CascadeClassifier('haarcascade_eye.xml')

eyes = casc.detectMultiScale(image)

for (x,y,w,h) in eyes:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 3)

cv2.waitKey()


