from ultralytics import YOLO
import cv2 


model = YOLO('/home/abdullah/abdullah-dev/object-segmentation/fruit/runs/segment/train7/weights/best.pt')
#model = YOLO('/home/abdullah/abdullah-dev/object-segmentation/fruit/runs/detect/train/weights/best.pt')


cap=cv2.VideoCapture('/home/abdullah/abdullah-dev/object-segmentation/fruit/orange-catch.mp4')


if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Process each frame
while True:
    ret, frame = cap.read()
    if not ret:
        break
    target_width = 640
    target_height = 640
    resized_frame = cv2.resize(frame, (target_width, target_height))

    # Run YOLO model on the frame
    results = model.track(frame,conf=0.7,imgsz=640)
    
    # Display the frame
    annotated_frame = results[0].plot()  # Draw bounding boxes on the frame
    cv2.imshow("YOLOv8 Detection", annotated_frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
