import numpy as np
import cv2

cap=cv2.VideoCapture(0)

fourcc=cv2.cv.CV_FOURCC(*'XVID')
out=cv2.VideoWriter('myfuckingface.avi',fourcc,30.0,(640,480))

while(cap.isOpened()):
    ret,frame = cap.read()
    cv2.imshow('normal',frame)
    if(ret == True):
        frame = cv2.flip(frame,0)
        out.write(frame)
        cv2.imshow('flippedvideo',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
