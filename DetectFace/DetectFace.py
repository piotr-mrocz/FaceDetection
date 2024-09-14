import cv2 #openCV

camera = 0; # select camera in you device

capture = cv2.VideoCapture(camera)

heightWindow = 480
widthWindow = 640
frameName = 'My camera'
rgbZielony = (0, 128, 0)
thickness = 5


capture.set(cv2.CAP_PROP_FRAME_HEIGHT, heightWindow)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, widthWindow)

faceDetector = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

while True:
    # capture.read() returns 2 values: first value from video; second just picture from camera
    _, img = capture.read()
    
    # reactreate frame but only in gray colors
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # face detection
    faces = faceDetector.detectMultiScale(
        grayImg,
        scaleFactor = 1.2,
        minNeighbors = 4,
        minSize = (50, 50)
    )
    
    for x, y, face_width, face_height in faces:
        cv2.rectangle(img, (x, y), (x + face_width, y + face_height), rgbZielony, thickness)

    cv2.imshow(frameName, img)
    
    timeout = 50;
    key = cv2.waitKey(timeout)
    
    escapeKeyValue = 27;

    if key == escapeKeyValue or cv2.getWindowProperty(frameName, cv2.WND_PROP_VISIBLE) < 1:
        break

# release values
capture.release()