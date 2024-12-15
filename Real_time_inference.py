from ultralytics import YOLO
import cv2
import torch

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

    # Convert frame (optional resizing for better speed)
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Perform inference
    results = model.predict(source=img, save=False, conf=0.5)  # Predict directly on the frame

    # Access predictions
    for result in results:
        boxes = result.boxes  # Bounding boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())  # Bounding box coordinates
            conf = box.conf[0].item()  # Confidence score
            cls = int(box.cls[0].item())  # Class label
            label = f"{model.names[cls]} {conf:.2f}"  # Get class name

            # Draw bounding box and label on frame
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Show the annotated frame
    cv2.imshow("YOLO Real-Time Inference", frame)

    # Break the loop on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
