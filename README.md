# OpenCV Canlı Yüz Tespiti (Haar Cascade)

Bu proje, **Python ve OpenCV** kullanılarak bilgisayar kamerası üzerinden **gerçek zamanlı yüz tespiti** yapılmasını sağlar. Projede, OpenCV’nin klasik ve hâlâ yaygın olarak kullanılan **Haar Cascade (CascadeClassifier)** yöntemi kullanılmıştır.

Proje; bilgisayarlı görü (Computer Vision) alanına giriş yapmak isteyenler için **temel–orta seviye**, öğretici ve sade bir örnek sunar.

---

## 🚀 Özellikler

* Gerçek zamanlı kamera görüntüsü
* Haar Cascade algoritması ile yüz tespiti
* Aynı anda birden fazla yüz algılama
* Düşük donanım gereksinimi
* Anlaşılır ve düzenli kod yapısı

---

## 🧠 Kullanılan Teknolojiler

* **Python 3.x**
* **OpenCV (cv2)**
* **Haar Cascade Classifier**

---

## 📂 Proje Yapısı

```
.
├── main.py
├── haarcascadefrontalface.xml
├── README.md
```

* `main.py` : Ana Python uygulama dosyası
* `haarcascadefrontalface.xml` : Eğitilmiş yüz tespit modeli
* `README.md` : Proje dokümantasyonu

---

## ⚙️ Kurulum

### 1️⃣ Gerekli Kütüphaneyi Yükle

```bash
pip install opencv-python
```

### 2️⃣ Haar Cascade Modelini İndir

OpenCV’nin resmi Haar Cascade deposundan `haarcascadefrontalface.xml` dosyasını indirip, `main.py` ile **aynı klasöre** ekleyin.

---

## ▶️ Kullanım

Projeyi çalıştırmak için terminal veya komut satırında aşağıdaki komutu kullanın:

```bash
python main.py
```

* Kamera otomatik olarak açılır
* Algılanan yüzler mavi dikdörtgen ile işaretlenir
* Çıkmak için **Q** tuşuna basın

---

## 🔍 Nasıl Çalışır?

1. Kamera `cv2.VideoCapture()` ile açılır
2. Kameradan sürekli kareler (frame) alınır
3. Görüntü gri tona dönüştürülür
4. Haar Cascade modeli ile yüzler tespit edilir
5. Tespit edilen yüzlerin etrafına dikdörtgen çizilir
6. Görüntü gerçek zamanlı olarak ekranda gösterilir

---

## 📌 Teknik Notlar

* Haar Cascade algoritması **gri görüntü** üzerinde çalışır
* `scaleFactor` ve `minNeighbors` parametreleri doğruluk ve performansı doğrudan etkiler
* Bu yöntem, derin öğrenme tabanlı modellere göre daha basit ancak oldukça hızlıdır

---

## 🧪 Geliştirme Fikirleri

* Göz ve gülümseme tespiti ekleme
* FPS (Frame Per Second) hesaplama
* Derin öğrenme (DNN / CNN) tabanlı yüz tespiti
* Yüz tanıma (Face Recognition)
* Video dosyası üzerinden yüz analizi

---

## 📜 Lisans

Bu proje **MIT Lisansı** altında paylaşılmaktadır. Eğitim ve kişisel projelerde özgürce kullanılabilir.

---

## ✍️ Not

Bu proje, OpenCV ve bilgisayarlı görü alanına sağlam bir temel atmak amacıyla hazırlanmıştır. Kod yapısı sade tutulmuş ve öğrenmeye odaklanılmıştır.
