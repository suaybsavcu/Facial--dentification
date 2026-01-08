# OpenCV kütüphanesini projeye dahil ediyoruz.
import cv2

# Yüz tanıma için haar cascade modelinin yüklüyoruz.
face_cascade = cv2.CascadeClassifier("haarcascadefrontalface.xml")

# Kamerayı açıyoruz (0 = varsayılan kamera)
camera = cv2.VideoCapture(0)

while True:
    # Kameradan bir kare al
    ret, frame = camera.read()

    # Kamera görüntü vermezse çık
    if ret == False:
        break

    # Görüntüyü gri tona çevir
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüzleri tespit et
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Bulunan yüzlerin etrafına dikdörtgen çiz
    for(x, y, w, h) in faces:
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (255, 0, 0),
            2
    )

# Görüntüyü ekranda göster
cv2.imshow("Canli yuz Tespitti", frame)

# Kaynakları Serbest bırak
camera.release()
cv2.destroyAllWindows()
