from mtcnn import MTCNN
import cv2
class FaceDetectorWithCNN:
    def __init__(self):
        self.detector=MTCNN()
    def detect(self,image):
        image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        faces=self.detector.detect_faces(image)
        return faces
