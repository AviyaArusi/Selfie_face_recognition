"""
# Face Recognition with Multiprocessing

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen)

A Python script that uses the `face_recognition` library to identify photos containing a specific person's face from a directory of images. The script leverages **multiprocessing** for faster processing, making it ideal for handling large datasets.

---

## Features

- Detects and matches faces in images using the `face_recognition` library.
- Processes images concurrently using Python's `multiprocessing` module.
- Copies matched images into a designated output folder.
- Handles errors gracefully, skipping problematic images without stopping execution.

---

## Prerequisites

### Requirements

1. **Python**: Version 3.7 or higher
2. **Required Libraries**:
   - `face_recognition`
   - `numpy`
   - `dlib`
   - `shutil`

   Install the required libraries using pip:

   ```bash
   pip install face_recognition numpy dlib


## How to Use

Follow these steps to run the face recognition script:

```bash
git clone https://github.com/AviyaArusi/Selfie_face_recognition.git
cd Selfie_face_recognition

python faceRecognition.py
