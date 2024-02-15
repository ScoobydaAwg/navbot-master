# FaceDetector.py
import cv2 as cv

def detect_faces():
    capture = cv.VideoCapture(0)  # Open default camera

    # Load the custom model for face detection
    pretrained_model = cv.CascadeClassifier("Facedata.xml")

    face_detected = False
    while True:
        ret, frame = capture.read()
        if ret:
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            faces = pretrained_model.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

            if len(faces) > 0:
                face_detected = True
                # Draw rectangle around the first detected face and show it
                x, y, w, h = faces[0]
                cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv.imshow("Live Face Detection", frame)
                cv.waitKey(1)  # Display the frame for a moment so the user can see the detection
                break  # Exit the loop as soon as a face is detected

    capture.release()
    cv.destroyAllWindows()
    return face_detected
