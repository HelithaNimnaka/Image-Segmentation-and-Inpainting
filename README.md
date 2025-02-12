# Image-Segmentation-and-Inpainting

This project focuses on **real-time human segmentation and inpainting**, designed to detect and remove humans from video frames.

## Semantic Segmentation

Semantic segmentation is a deep learning technique that classifies each pixel in an image into a specific category, allowing for a more detailed understanding of image content. Unlike instance segmentation, which differentiates between individual objects of the same class, semantic segmentation assigns the same label to all objects of the same category.

The output of a semantic segmentation model includes:
- A pixel-wise mask where each pixel is assigned a class label.
- No distinction between different instances of the same class.

Semantic segmentation is particularly useful for tasks like background removal, scene understanding, and video inpainting.

---

## Table of Contents

- [Setup Camera](#setup-camera)
- [Pretrained Models](#pretrained-models)
- [Installation](#installation)
- [Real-Time Segmentation](#real-time-segmentation)
- [Real-Time Inpainting for Humans](#real-time-inpainting-for-humans)
- [Inpainting Methods](#inpainting-methods)
- [Use Case Reference](#use-case-reference)

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

The following demonstrates **real-time human segmentation**, where each pixel in video frames is classified into a category, helping to distinguish humans from the background.

![Segmentation Output](Images/Real_time_segmentation.gif "Segmentation Output")

---

## Real-Time Inpainting for Humans

This section demonstrates **real-time inpainting**, where humans are detected in video frames and removed seamlessly.

We use **OpenCV's inpainting methods**, which include:
- **Telea's Inpainting Algorithm (`cv2.INPAINT_TELEA`)** – Based on fast marching methods for smooth reconstruction.
- **Navier-Stokes Based Inpainting (`cv2.INPAINT_NS`)** – Uses a fluid dynamics-based approach for structure propagation.

Additionally, deep learning-based **inpainting models** can be integrated for higher-quality results, particularly for complex textures and larger missing regions.

![Inpainting Example](Images/RealTimeInpainting.gif "Inpainting Example")

---

## Inpainting Methods

We employ **OpenCV's inpainting methods** and **deep learning-based inpainting models** to achieve high-quality results. Depending on the use case, different techniques can be applied:

### 1. **OpenCV Inpainting**
   - **Telea's Algorithm (`cv2.INPAINT_TELEA`)**  
   - **Navier-Stokes Inpainting (`cv2.INPAINT_NS`)**

### 2. **Deep Learning-Based Inpainting**
   - GAN-based models (Generative Adversarial Networks)  
   - Transformer-based inpainting  
   - Context-aware inpainting networks  

By combining these approaches, we can significantly improve **inpainting quality, restore missing regions seamlessly, and preserve background textures**.

---

## Use Case Reference

Inpainting techniques have been widely used in various applications, including **Visual SLAM and signal enhancement**. A notable research paper on **GAN-based Image Inpainting** explores improving SLAM performance with inpainting:

[📄 From Augmentation to Inpainting: Improving Visual SLAM with Signal Enhancement Techniques and GAN-based Image Inpainting](https://www.researchgate.net/publication/378914308_From_Augmentation_to_Inpainting_Improving_Visual_SLAM_with_Signal_Enhancement_Techniques_and_GAN-based_Image_Inpainting)

This research demonstrates how **image inpainting can enhance robotic vision, scene understanding, and mapping quality**.

---

