import cv2

# video dosyası veya kameradan görüntü yakalama
cap = cv2.VideoCapture(0)

# fark alma algoritması için önceki çerçeve
_, prev_frame = cap.read()
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

# hareket tespiti için eşik değeri
thresh = 10000

while True:
    # yeni bir kare okuyun ve gri tona dönüştürün
    ret, new_frame = cap.read()
    new_gray = cv2.cvtColor(new_frame, cv2.COLOR_BGR2GRAY)
    
    # fark alma algoritması ile hareketi tespit edin
    diff = cv2.absdiff(prev_gray, new_gray)
    _, binary = cv2.threshold(diff, thresh, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # tespit edilen her bir hareket için bir dikdörtgen çizin
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(new_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # çıktıyı gösterin
    cv2.imshow('frame', new_frame)
    prev_gray = new_gray
    
    # q tuşuna basarak programı durdurun
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# çıkış
cap.release()
cv2.destroyAllWindows()
