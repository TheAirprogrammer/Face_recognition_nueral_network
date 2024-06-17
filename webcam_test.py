import cv2
import uuid
import os

ANC_PATH = 'data/anchor'
POS_PATH = 'data/positive'
INP_PATH = 'app_data/input_image'

def save_image(path, frame):
    """Saves the frame to the specified path."""
    imgname = os.path.join(path, '{}.jpg'.format(uuid.uuid1()))
    _, buffer = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
    with open(imgname, 'wb') as f:
        f.write(buffer)
    return imgname

# Establish a connection to the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
else:
    try:
        while cap.isOpened():
            ret, frame = cap.read()
            
            # Corrected frame cropping to 250x250 pixels
            height, width, _ = frame.shape
            center_y = height // 2
            center_x = width // 2
            cropped_frame = frame[max(0, center_y - 125):min(height, center_y + 125),
                                 max(0, center_x - 125):min(width, center_x + 125)]
            
            key = cv2.waitKey(1) & 0xFF
            if key == ord('a'):  # Collect anchor
                save_image(ANC_PATH, cropped_frame)
            elif key == ord('p'):  # Collect positive
                save_image(POS_PATH, cropped_frame)
            if not ret:
                print("Error: Failed to capture image.")
                break
            
            cv2.imshow('ImageCollection', cropped_frame)
            
            if key == ord('q'):  # Exit condition
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()
