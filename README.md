# Underwater-ROV

[![Language](https://img.shields.io/badge/Language-Python-yellow.svg?style=for-the-badge)](https://en.wikipedia.org/wiki/Programming_language)

This project presents a Python-based control system for an **Underwater ROV (Remotely Operated Vehicle)**. It appears to integrate core motor and camera control, computer vision (possibly object detection using YOLO), and modules for data handling and microcontroller interfacing. The goal is likely to provide semi-autonomous or teleoperated underwater exploration or inspection capabilities.

---

## 📚 Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

---

## 🚀 Features

From the directory and file names (`ai_training/`, `main_nodemcu/`, `custom_dataset/`, `best.pt`), the project likely includes the following:

- **ROV Control System**:
  - Python code for maneuvering the underwater vehicle.
  - Integration with motor controllers (e.g., via `main_nodemcu/`).
  
- **AI-Based Object Detection**:
  - Uses a pre-trained model (`best.pt`) for detecting underwater objects or obstacles.
  - May use YOLOv5 or YOLOv8 architecture (check inside `ai_training/`).

- **Custom Dataset Support**:
  - Mechanisms for training or fine-tuning models on underwater-specific imagery (`custom_dataset/`).

- **Camera and Video Stream Handling**:
  - Capture, process, and possibly display video from underwater cameras.
  - Object detection overlays, logging, or decision making.

- **Modular Architecture**:
  - Clean separation between hardware interfacing, model prediction, and data processing components.

---

## 🧰 Technologies Used

- **Language**: Python
- **Likely Libraries**:
  - `opencv-python` (for camera & video processing)
  - `torch`, `ultralytics` or `YOLOv5` repo (for object detection models)
  - `numpy`, `pandas` (for data handling)
  - `serial` or `pyserial` (for communication with NodeMCU or similar microcontrollers)

> You can verify exact dependencies in `requirements.txt`, if provided.

---

## ⚙️ Installation

To set up and run the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/underwater-rov.git
cd underwater-rov
```

### 2. Install Python Dependencies
If a `requirements.txt` file is present:
```bash
pip install -r requirements.txt
```

If not, you may need to install expected libraries manually:
```bash
pip install opencv-python torch numpy pyserial
```

---

## ▶️ Usage

### Running the Main ROV Control System
```bash
python main.py
```

This script may:
- Initialize the video stream
- Load the object detection model (`best.pt`)
- Establish serial communication with the microcontroller
- Start navigation and object detection loop

### Exploring Specific Modules

- **AI Training / Fine-tuning**
  - Look into the `ai_training/` directory to train a model on custom underwater data.
  - Dataset should be in YOLO format if using YOLOv5/YOLOv8.

- **Microcontroller Communication**
  - The `main_nodemcu/` folder likely contains embedded code (e.g., Arduino/ESP8266) for hardware interfacing with motors, sensors, etc.

---

## 🧪 Example Workflow

```bash
# Run the ROV software
python main.py --source 0 --model best.pt
```

*Check inside `main.py` or supporting scripts for additional flags like serial port configuration, camera index, or resolution settings.*

---

## 🤝 Contributing

Want to make this better? Contributions are welcome!

1. Fork the repository
2. Create a new branch:
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add AmazingFeature"
   ```
4. Push to GitHub:
   ```bash
   git push origin feature/AmazingFeature
   ```
5. Create a pull request describing your changes

---

## 📌 Notes

- For real-world deployment, waterproofing, camera placement, motor calibration, and buoyancy tuning are crucial.
- Consider logging GPS data, depth sensors, or even IMU integration for advanced features.
- AI inference can be offloaded to edge devices (e.g., Jetson Nano, Raspberry Pi with Coral TPU).

---

