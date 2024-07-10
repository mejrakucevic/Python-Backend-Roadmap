import cv2

detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
impImg = cv2.VideoCapture("elon.jpg")

res, img = impImg.read()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = detect.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)

# img = cv2.imread("ts.jpg")

cv2.imshow("Elon Musk", img)

cv2.waitKey(0)
impImg.release()
cv2.destroyAllWindows()