
""""
capture frames from webcam to create a dataset
"""
import os

import cv2

save_path = "raw_data"
label_path = os.path.join(save_path, "labels")
os.makedirs(save_path, exist_ok=True)
os.makedirs(label_path, exist_ok=True)

cap = cv2.VideoCapture(0)
i = len(os.listdir("data/images"))

import time
start = time.time()

while True:
    ret, frame = cap.read()
    cv2.imshow("frame", frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
    if time.time() - start > 1.0:
        cv2.imwrite(os.path.join(save_path, f"{i}.jpg"), frame)
        i += 1
        with open(os.path.join(label_path, f"{i}.txt"), "w") as f:
            pass
        start = time.time()
        print(f"captured {i} frames")
