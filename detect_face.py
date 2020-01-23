import cv2


URL="http://192.168.11.14:8081/?action=stream"

capture = cv2.VideoCapture(URL)

INTERVAL= 33

cascade_file = "haarcascade_frontalface_default.xml"
cascade = cv2.CascadeClassifier(cascade_file)

ratio = 1/15

while True:

    ret, frame = capture.read()
    faces = cascade.detectMultiScale( frame, minSize=(100, 100) )

    for x, y, w, h in faces:
        face = frame[ y:y+h, x:x+w ]
        small = cv2.resize( face, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST )
        frame[ y:y+h, x:x+w ] = cv2.resize( small, (w,h), interpolation=cv2.INTER_NEAREST )
        color = ( 0, 0, 225 )
        pen_w = 3
        cv2.rectangle( frame, (x, y), (x+w, y+h), color, thickness=pen_w )

    cv2.imshow( 'frame', frame )

    key = cv2.waitKey( INTERVAL ) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()

