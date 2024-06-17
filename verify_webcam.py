import cv2

def capture_and_save_frame(frame_path):
    cap = cv2.VideoCapture(0)
    try:
        while cap.isOpened():
            ret, frame = cap.read()
            height, width, _ = frame.shape
            center_y = height // 2
            center_x = width // 2
            frame = frame[max(0, center_y - 125):min(height, center_y + 125), max(0, center_x - 125):min(width, center_x + 125)]
            cv2.imshow('ImageCollection', frame)
            if cv2.waitKey(1) & 0xFF == ord('v'):  # Press 'v' to capture the frame
                cv2.imwrite(frame_path, frame) # Save the frame as an image
                break  
            elif cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if not ret:
                print("Error: Failed to capture image.")
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

frame_path = 'app_data/input_image/input_image.jpg'
capture_and_save_frame(frame_path)

