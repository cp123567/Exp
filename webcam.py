import cv2
# Method to create videoCapture object.(It'll trigger the camera)
cap=cv2.VideoCapture(0) #Here, '0' is to specify that use built-in-camera
while True:
    _, frame=cap.read()
    height, width= frame.shape[:2]
    #gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capture",frame)
    key=cv2.waitKey(1) # It'll generate a new frame after every 1 ms.
    if key == ord('q'): 
        break
cap.release()
cv2.destroyAllWindows()





