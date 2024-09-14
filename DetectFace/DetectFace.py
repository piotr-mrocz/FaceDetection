import cv2 #openCV

camera = 0; # select camera in you device

capture = cv2.VideoCapture(camera)

heightWindow = 480
widthWindow = 640

capture.set(cv2.CAP_PROP_FRAME_HEIGHT, heightWindow)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, widthWindow)

while True:
    # capture.read() returns 2 values: first value from video; second just picture from camera
    _, img = capture.read()
    cv2.imshow('My picure', img)
    
    timeout = 50;
    key = cv2.waitKey(timeout)
    
    escapeKeyValue = 27;

    if key == escapeKeyValue:
        break

# release values
capture.release()