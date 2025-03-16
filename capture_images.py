import cv2
import os

gestures = ["thumbs_up", "thumbs_down"]  # Both gestures
dataset_path = "dataset"
os.makedirs(dataset_path, exist_ok=True)

cap = cv2.VideoCapture(0)
gesture_index = 0  # Start with "thumbs_up"
count = 0
collecting = False  # Start only when 'S' is pressed

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Overlay green counter
    cv2.putText(frame, f"Gesture: {gestures[gesture_index]}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f"Images: {count}/200", (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Capture Gesture", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):  # Start collecting
        collecting = True
        os.makedirs(f"{dataset_path}/{gestures[gesture_index]}", exist_ok=True)
        print(f"Collecting images for {gestures[gesture_index]}...")

    if collecting and count < 200:
        cv2.imwrite(f"{dataset_path}/{gestures[gesture_index]}/{count}.jpg", frame)
        count += 1
    elif collecting and count >= 200:
        collecting = False
        count = 0
        gesture_index += 1  # Move to next gesture
        if gesture_index >= len(gestures):  # If all gestures are done
            break
        print(f"Switching to {gestures[gesture_index]}. Press 'S' to start.")

    if key == ord('q'):  # Quit anytime
        break

cap.release()
cv2.destroyAllWindows()
print("Image collection complete.")
