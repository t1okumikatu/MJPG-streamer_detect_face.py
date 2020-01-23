#!/usr/bin/env python

import cv2

URL="http://192.168.11.14:8081/?action=stream"
s_video = cv2.VideoCapture(URL)

while True:
  ret, img = s_video.read()
  cv2.imshow("Stream Video",img)
  key = cv2.waitKey(1) & 0xff
  if key == ord('q'): break 
  
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

