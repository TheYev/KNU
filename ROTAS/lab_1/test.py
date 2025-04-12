from ultralytics import YOLO


model = YOLO("weights/best.pt")  
result = model.predict("1.png", imgsz=640, show_boxes=True)  

for r in result:
    print(r.boxes)
    print(r.masks)
    print(r.keypoints)
    print(r.probs)
    print(r.obb)
    r.show()