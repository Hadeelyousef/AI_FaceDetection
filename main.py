# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam.
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# To use a video file as input
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Read the frame
    check, frame = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    # Draw the rectangle around each face
    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
    # Display
    cv2.imshow('img', frame)
    # Stop if escape key is pressed
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
