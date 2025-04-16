from ultralytics import YOLO
import argparse

#"C:/Users/thedi/OneDrive/Desktop/download.jpg"  
# C:/Users/thedi/OneDrive/Desktop/KNU/ROTAS/lab_1/1.png  
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True, help="Path to folde your photo")
    args = parser.parse_args()

    model = YOLO("weights/best.pt")  
    result = model.predict(args.path, imgsz=640, show_boxes=True)  

    for r in result:
        print(r.boxes)
        print(r.masks)
        print(r.keypoints)
        print(r.probs)
        print(r.obb)
        r.show()    
    
if __name__ == ("__main__"):
    main()