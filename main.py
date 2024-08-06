from ultralytics import YOLO
import cv2
import math
import pygame
import os

# Initialize Pygame for audio playback
pygame.init() 

# Load the YOLO model
model = YOLO('models/yolov8m_custom.pt')

# Define class names
classNames = [
    "dog", "person", "cat", "tv", "car", "meatballs", "marinara sauce",
    "tomato soup", "chicken noodle soup", "french onion soup", "chicken breast",
    "ribs", "pulled pork", "hamburger", "cavity", "20", "50", "100", "200", "500", "10"
]

# directory containing audio files
audio_dir = "./audio" 

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        continue
    # resizing image----------------------
    # img = cv2.resize(img, (640, 640))
    results = model(img, stream=True)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            conf = math.ceil((box.conf[0] * 100)) / 100
            if conf >= 0.65:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            
                cls = int(box.cls[0])
                class_name = classNames[cls]
                label = f'{class_name} Rs. {conf}'
                t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
                c2 = x1 + t_size[0], y1 - t_size[1] - 3
                cv2.rectangle(img, (x1, y1), c2, [255, 0, 255], -1, cv2.LINE_AA)
                cv2.putText(img, label, (x1, y1 - 2), 0, 1, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)

                # Play audio if object class is detected
                audio_file = os.path.join(audio_dir, f"{class_name}.mp3")
                if os.path.exists(audio_file):
                    pygame.mixer.music.load(audio_file)
                    pygame.mixer.music.play()

    cv2.imshow("CurrenSee", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
pygame.mixer.quit()
cap.release()
cv2.destroyAllWindows()