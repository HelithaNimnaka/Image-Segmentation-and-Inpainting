# Image-Segmentation-and-Inpainting

This project focuses on **real-time human segmentation and inpainting**, designed to detect and remove humans from video frames.

Instance segmentation goes beyond object detection by identifying individual objects in an image and segmenting them from the rest of the image. 

The output of an instance segmentation model includes:
- A set of masks or contours outlining each object in the image.
- Class labels and confidence scores for each object.

Instance segmentation is particularly useful when you need to understand not only where objects are located in an image but also their exact shape.

---

## Table of Contents

- [Setup Camera](#setup-camera)
- [Pretrained Models](#pretrained-models)
- [Installation](#installation)
- [Real-Time Segmentation](#real-time-segmentation)
- [Real-Time Inpainting for Humans](#real-time-inpainting-for-humans)

---

## Setup Camera

You can use your mobile phone as a web camera via WiFi. Follow these steps:

1. Download the **DroidCam app** on your phone.  
2. Install the **DroidCam Client** on your computer.  
3. Link the phone app and the computer client following the instructions provided [here](https://droidcam.app/).

---

## Pretrained Models

For this project, the **YOLO11n-seg** pretrained model is used. Refer to the official documentation for more details: [Ultralytics Segmentation](https://docs.ultralytics.com/tasks/segment/).

---

## Real-Time Segmentation

The following demonstrates **real-time human segmentation**, where individuals in video frames are detected and their contours are identified.

![Segmentation Output](images/Real_time_segmentation.gif "Segmentation Output")

---

## Real-Time Inpainting for Humans

This section demonstrates **real-time inpainting**, where humans are detected in video frames and removed seamlessly.

![Inpainting Example](images/Real_time_inpainting.gif "Inpainting Example")

---

