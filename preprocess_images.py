import cv2
import os

input_folder = "dataset"
output_folder = "processed_dataset"
img_size = (64, 64)  # Change if needed

os.makedirs(output_folder, exist_ok=True)

for gesture in os.listdir(input_folder):
    gesture_path = os.path.join(input_folder, gesture)
    save_path = os.path.join(output_folder, gesture)
    os.makedirs(save_path, exist_ok=True)

    for img_name in os.listdir(gesture_path):
        img_path = os.path.join(gesture_path, img_name)
        img = cv2.imread(img_path)

        if img is None:
            continue  # Skip unreadable images

        img = cv2.resize(img, img_size)  # Resize
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

        cv2.imwrite(os.path.join(save_path, img_name), img_gray)

print("✅ Preprocessing complete. Images saved in 'processed_dataset/'.")
