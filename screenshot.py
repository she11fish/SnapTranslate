# Import essential libraries
import requests
import cv2
import numpy as np
import imutils
import pytesseract
from tools import user_accepts, snapTranslate
import random
  
def screenshot():
    url = "http://192.168.2.20:8080/shot.jpg"

    pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract\tesseract.exe"
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
    cv2.imshow(str(random.randint(0, 1000000)), img)

    # Press Esc key to exit
    if cv2.waitKey(1) == 27:
        pass
    if user_accepts():
        snapTranslate(data)

    return True