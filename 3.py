import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv2.line(img,(0,0),(511,511),(255,0,0),1)
cv2.line(img,(511,0),(0,511),(255,0,0),1)
while(1):
        
    cv2.imshow('image',img)
    if cv2.waitKey(1) & 0xff == ord('q'):
                break
cv2.imwrite('bello.jpg',img)
cv2.destroyAllWindows()

