# Hand Gesture Controlled Scrolling

## 🚀 Overview
This project allows hands-free scrolling using **thumbs-up** and **thumbs-down** gestures. Leveraging **MediaPipe** for hand tracking and a **custom-trained deep learning model**, it enables intuitive control over your screen.

## ✨ Features
- 👋 **Hands-Free Scrolling**: No need to touch the mouse or keyboard!
- 🎥 **Real-time Gesture Recognition**: Uses webcam input.
- 🖥️ **Smooth Integration**: Works on platforms like YouTube, websites, or documents.
- 🕒 **Automatic Delay Handling**: Prevents multiple scroll actions from a single gesture.

## 📂 Project Structure
```
📁 gesture-scroll
│── 📂 model/                 # Trained gesture recognition model
│── 📂 scripts/               # Helper scripts (data processing, training, etc.)
│── 📂 processed_data/        # Preprocessed images (ignored in Git)
│── 📂 dataset/               # Raw gesture images (ignored in Git)
│── ├── gesture_control.py    # Main script to run scrolling
│── ├── requirements.txt      # Dependencies
│── ├── README.md             # Project documentation
│── ├── .gitignore            # Ignore dataset and processed images
```

## 🔧 Installation
1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/gesture-scroll.git
   cd gesture-scroll
   ```
2. **Create a virtual environment**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

## 🎬 Usage
1. **Run the script**:
   ```sh
   python gesture_control.py
   ```
2. **Perform gestures**:
   - 👍 **Thumbs Up** → Scroll **UP**
   - 👎 **Thumbs Down** → Scroll **DOWN**
3. **Press `Q` to Quit.**

## 🤖 Training Your Own Model
1. Capture gesture images (thumbs-up & thumbs-down).
2. Train a CNN model using TensorFlow/Keras.
3. Save and integrate the model into `gesture_control.py`.

## 🛠️ Tech Stack
- **Python**
- **OpenCV** (Image Processing)
- **MediaPipe** (Hand Tracking)
- **TensorFlow/Keras** (Deep Learning)
- **PyAutoGUI** (Automating Mouse Scroll)



## 🌟 Contributing
Feel free to fork, improve, and submit pull requests! 😊




