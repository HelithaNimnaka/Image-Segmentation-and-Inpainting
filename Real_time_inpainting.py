from ultralytics import YOLO
import cv2
import numpy as np

# Load the YOLO model
model = YOLO("yolo11n-seg.pt")  # Load the custom or official YOLO model

# Set up webcam
cap = cv2.VideoCapture(0)  # Adjust index if necessary

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Starting real-time inference. Press 'q' to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to grab frame.")
        break

    # Convert frame to RGB (YOLO expects RGB images)
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Perform inference
    results = model.predict(source=img, save=False, conf=0.5)  # Predict directly on the frame

    # Extract class names and person index
    names_dict = results[0].names
    person_index = next((key for key, value in names_dict.items() if value == 'person'), None)
    persons = []

    if person_index is None:
        print("Person class not found in the class names.")
    else:
        for i, box in enumerate(results[0].boxes):  # Iterate through the detected boxes
            if int(box.cls) == person_index:  # Check if the class matches the person index
                persons.append(i)

    # Access masks for detected objects
    if hasattr(results[0], 'masks') and results[0].masks is not None:
        masks = results[0].masks.data.cpu().numpy()  # Convert tensor to NumPy array

        # Resize each mask to match the original image size
        resized_masks = [cv2.resize(mask, (frame.shape[1], frame.shape[0]), interpolation=cv2.INTER_NEAREST) for mask in masks]

        # Loop through resized masks and apply inpainting for persons
        for i, mask in enumerate(resized_masks):
            if i in persons:
                # Create a binary mask
                binary_mask = (mask > 0.5).astype(np.uint8)

                # Inpainting: Replace the masked region with inpainted values
                frame = cv2.inpaint(frame, binary_mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)

    # Display the annotated frame
    cv2.imshow("YOLO Real-Time Inference with Inpainting", frame)

    # Break the loop on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
