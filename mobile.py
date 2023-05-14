# Import essential libraries
import requests
import cv2
import numpy as np
import imutils
import pytesseract
from screenshot import screenshot
from threading import Thread
  
url = "http://192.168.2.20:8080/shot.jpg"

pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract\tesseract.exe"

def user_accepts():
    user_consent = input("Do you want to the ai to read the above text?:\n")
    if user_consent.lower() == "yes":
        return True
    if user_consent.lower() == "no":
        return False
    user_accepts()

threads = []
i = 0
while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=1000, height=1800)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    data = pytesseract.image_to_string(img)
    h, w, _ = img.shape
    boxes = pytesseract.image_to_boxes(img)
    for b in boxes.splitlines():
        b = b.split()
        cv2.rectangle(img, ((int(b[1]), h - int(b[2]))), ((int(b[3]), h - int(b[4]))), (0, 255, 0), 2)

    cv2.imshow("Android_cam", img)
  
    # Press Esc key to exit
    if cv2.waitKey(1) == 27:
        break
    
    if not threads:
        thread = Thread(target = screenshot, name="running" + str(i))
        thread.start()
        threads.append(thread)
    else:
        if not threads[0].is_alive():
            threads.pop()
    i += 1
  
cv2.destroyAllWindows()