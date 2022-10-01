import cv2
class face_detector:
    def __init__(self):
        self.cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    def detections(self,cap):
        gray=cv2.cvtColor(cap,cv2.COLOR_BGR2GRAY)
        face_coordinates=[]
        faces=self.cascade.detectMultiScale(gray,1.3,5)
        for face in faces:
            face_coordinates.append((face[0],face[1],face[2],face[3]))
        return face_coordinates
if "__main__"==__name__:
    capture=cv2.VideoCapture(0)
    det=face_detector()
    while True:
        _,frame=capture.read()
        faces=det.detections(frame)
        for face in faces:
            cv2.rectangle(frame,(face[0],face[1]),(face[0]+face[2],face[1]+face[3]),(0,255,0),2)
        frame=cv2.flip(frame,1)
        cv2.imshow("video",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()
