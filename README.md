# 🚗 Driver Drowsiness Detection System  

**A real-time AI-powered system to detect driver fatigue and prevent accidents.**  

## 📌 Overview  
Drowsy driving is a significant cause of road accidents. This project implements a **Driver Drowsiness Detection System** using **computer vision and machine learning** to monitor facial features and alert the driver when drowsiness is detected.  

## 🔬 Features  
✔ **Real-time detection** using a webcam  
✔ **Facial landmark tracking** with **Ensemble of Regression Trees (ERT)**  
✔ **Eye blink frequency & head tilt monitoring**  
✔ **Instant alerts with sound warnings**  
✔ **Works without intrusive sensors**  

## 🛠️ Technologies Used  
- **Programming Language**: Python 3.9  
- **Libraries**: OpenCV, Dlib, Imutils, Numpy, Scikit-learn, Matplotlib, Flask  
- **Algorithm**: Ensemble of Regression Trees (ERT)  
- **Hardware Requirements**:  
  - Camera (for real-time video processing)  
  - Speaker (for audio alerts)  

## 📂 Project Structure  
📦 Driver-Drowsiness-Detection
┣ 📁 dataset/ # Training images and facial landmarks
┣ 📁 models/ # Trained ML models
┣ 📜 requirements.txt # Required Python packages
┣ 📜 drowsiness_detector.py # Main script
┣ 📜 utils.py # Helper functions
┣ 📜 README.md # Project documentation


## 📊 System Workflow  
1. **Capture video** from a webcam.  
2. **Detect facial features** using **ERT (Ensemble of Regression Trees)**.  
3. **Analyze eye blinking rate & head movements**.  
4. **Trigger an alert** if drowsiness is detected.  

## 🔍 Existing vs. Proposed System  
| Feature | Existing Systems | Proposed System |
|---------|-----------------|----------------|
| **Detection Method** | Sensor-based | Computer Vision |
| **Accuracy** | Moderate | High (Real-time ERT) |
| **Intrusiveness** | Requires wearable sensors | No sensors needed |
| **Alert Mechanism** | Limited | Instant sound alert |

📢 Results & Performance
Highly accurate detection using ERT-based face tracking
Works in real-time with minimal lag
No additional hardware required except a webcam
📬 Contact
📍 Developer: Arunkumar A
📧 Email: akarun1527@gmail.com
🔗 LinkedIn: https://www.linkedin.com/in/arunkumar-a-06b437250
🌍 GitHub: Arunkumar1527

