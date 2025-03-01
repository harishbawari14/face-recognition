# FACE RECOGNITION ATTENDANCE SYSTEM

## Overview

This project is a Face Recognition-based Attendance System using Python and OpenCV. It captures faces from a webcam, compares them with stored images, and logs attendance in a CSV file.

## 📂 Features

✅ Real-time face recognition using OpenCV & dlib  
✅ Automatic attendance marking in a CSV file  
✅ Works with multiple known faces  
✅ Displays the detected person's name on the screen  
✅ Simple and efficient implementation  

## 🛠️ Installation

### Prerequisites

Make sure you have **Python 3.10+** installed. You also need to install the following dependencies:

```sh
pip install opencv-python numpy dlib face_recognition
```

### Installing dlib (If Required)

If you face issues with dlib, install it manually:

```sh
pip install cmake
pip install dlib
```

## 🚀 Usage

### Place Images
Store known faces inside the `faces/` directory.

### Run the Script

```sh
python face_attendance.py
```

### Mark Attendance
The system will detect known faces and log attendance in a CSV file (named as per the current date).

Press **'Q'** to exit the program.

## 📝 CSV Output Format

Each attendance record is saved as a CSV file (**YYYY-MM-DD.csv**) with:

```
Name, Time
Harish, 10:15:32
Nick, 10:20:45
```

## ⚙️ Project Structure

```
FaceRecognition/
│-- face_attendance.py  # Main script
│-- faces/              # Folder to store known face images
│   │-- harish.jpg
│   │-- nick.avif
│-- requirements.txt    # Dependency list
```
