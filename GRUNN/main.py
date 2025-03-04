import cv2
import mediapipe as mp


# Ініціалізація MediaPipe для відстеження рук
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Ініціалізація моделі Hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5)

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Не вдалося відкрити камеру")
    exit()

while True:
    ret, frame = cam.read()
    if not ret:
        print("Не вдалося зчитати кадр")
        break

    # Перетворення BGR -> RGB (MediaPipe працює з RGB)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Обробка кадру моделлю
    results = hands.process(frame_rgb)

    # Візуалізація детекції рук
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2))

    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
