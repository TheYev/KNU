import pyautogui as pag

import cv2
import torch
import torchvision

from non_max import non_max_suppression

model_path = "C:/Users/thedi/OneDrive/Desktop/KNU/ROTAS/lab2/best.torchscript"
model = torch.jit.load(model_path)
model.eval()


def detect_on_image(image):
    image = image[:, ::-1, :]
    image = cv2.copyMakeBorder(image, 80, 80, 0, 0, cv2.BORDER_CONSTANT, value=(0, 0, 0))
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_tensor = torchvision.transforms.ToTensor()(rgb_image)
    image_tensor = image_tensor.unsqueeze(0)
    pred = model(image_tensor)
    pred = non_max_suppression(pred)[0]
    if not len(pred):
        return image, None, None, None, None
    x_min, y_min, x_max, y_max = pred[0][:4]
    y_min, x_min, y_max, x_max = int(y_min), int(x_min), int(y_max), int(x_max)
    return image, y_min, x_min, y_max, x_max


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    mouse_pos = list(map(int, pag.position()))
    sign_pos = [None, None]
    move = [0, 0]
    click_count = 0
    while True:
        ret, frame = cap.read()
        image, y_min, x_min, y_max, x_max = detect_on_image(frame)
        if y_min is not None:
            if sign_pos[0] is None:
                sign_pos = [x_min, y_min]
            else:
                move = [move[0] + (x_min - sign_pos[0])*2.5, move[1] + (y_min - sign_pos[1])*2.5]
                if abs(move[0]) > 10 or abs(move[1]) > 10:
                    mouse_pos = [mouse_pos[0] + move[0], mouse_pos[1] + move[1]]
                    mouse_pos[0] = max(0, min(1919, mouse_pos[0]))
                    mouse_pos[1] = max(0, min(1079, mouse_pos[1]))
                    try:
                        pag.moveTo(mouse_pos[0], mouse_pos[1], 0)
                    except:
                        pass
                    move = [0, 0]
                sign_pos = [x_min, y_min]
        else:
            if sign_pos[0] is not None:
                click_count += 1
            elif click_count > 0:
                click_count += 1
            if click_count > 15:
                try:
                    pag.click()
                except:
                    pass
                click_count = 0
            print("No sign")
            sign_pos = [None, None]
        # point on image
        cv2.circle(image, (sign_pos[0], sign_pos[1]), 5, (0, 0, 255), -1)
        cv2.imshow("frame", image)
        k = cv2.waitKey(1)