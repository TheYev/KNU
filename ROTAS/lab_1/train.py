from ultralytics import YOLO


model = YOLO("yolov8m.pt")
model.train(data="dataset/data.yaml", epochs=100, imgsz=640, batch=16, model="yolov8m.pt")
