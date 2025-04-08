import torch
from ultralytics import YOLO

model = YOLO('yolov8n.pt')
model.train(
        data='C:/Users/thedi/OneDrive/Desktop/KNU/ROTAS/lab2/datasets/data.yaml', 
        epochs=50, 
        imgsz=640, 
        batch=16, 
        model="yolov8n.pt",
        device='0',
        )