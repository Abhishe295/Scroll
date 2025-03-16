import cv2
import numpy as np
import tensorflow as tf
import mediapipe as mp
import pyautogui
import time
import gc

# Load the trained model
model = tf.keras.models.load_model('gesture_model.h5')

# Initialize MediaPipe Hand Detection
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7)

# Define labels
labels = ["Thumbs Down", "Thumbs Up"]

# Start webcam
cap = cv2.VideoCapture(0)

# Initialize tracking variables
last_action_time = time.time()
idle_threshold = 300  # 5 minutes before auto-exit
scroll_delay = 1  # 1 second delay between actions

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        print("Webcam disconnected or frame capture failed.")
        break

    # Flip frame for natural feel
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hands
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Extract hand bounding box
            x_min = int(min([lm.x for lm in hand_landmarks.landmark]) * frame.shape[1])
            y_min = int(min([lm.y for lm in hand_landmarks.landmark]) * frame.shape[0])
            x_max = int(max([lm.x for lm in hand_landmarks.landmark]) * frame.shape[1])
            y_max = int(max([lm.y for lm in hand_landmarks.landmark]) * frame.shape[0])

            # Ensure bounding box is within frame
            x_min, x_max = max(0, x_min), min(frame.shape[1], x_max)
            y_min, y_max = max(0, y_min), min(frame.shape[0], y_max)

            # Crop hand region
            hand_img = frame[y_min:y_max, x_min:x_max]

            # Ensure valid image
            if hand_img.size == 0:
                print("Warning: Empty hand region detected, skipping frame.")
                continue

            # Resize & preprocess for the model
            hand_img = cv2.resize(hand_img, (64, 64))
            hand_img = np.expand_dims(hand_img, axis=0) / 255.0

            # Predict gesture
            prediction = model.predict(hand_img)
            label = labels[int(prediction[0] > 0.5)]  # 0 = Thumbs Down, 1 = Thumbs Up

            # Scroll action with delay
            current_time = time.time()
            if current_time - last_action_time > scroll_delay:
                if label == "Thumbs Up":
                    pyautogui.scroll(300)  # Scroll up
                    print("Scrolling Up")
                elif label == "Thumbs Down":
                    pyautogui.scroll(-300)  # Scroll down
                    print("Scrolling Down")
                
                last_action_time = current_time  # Update last action time
            
            # Display result
            cv2.putText(frame, label, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Free memory
            gc.collect()

    else:
        print("No hand detected. Waiting...")

    # Auto-exit if inactive for too long
    if time.time() - last_action_time > idle_threshold:
        print("No gesture detected for 5 minutes. Exiting...")
        break

    # Show the output
    cv2.imshow("Gesture Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

#venv\Scripts\activate