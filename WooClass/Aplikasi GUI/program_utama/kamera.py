import cv2
from 

class Kamera:

    def __init__(self, index):
        self.kamera = cv2.VideoCapture(index)
        
    def membaca_frame(self):

        while(True):

            _, frame = self.kamera.read()
        
            self.roi_frame = frame[0:475, 110:480]
        
            cv2.rectangle(frame, (110,0), (480,475), (0,0,0), 1)
        
            cv2.imshow("Frame Original",frame)

            if(cv2.waitKey(1) & 0xFF == ord('q')):
                break
            
            return self.roi_frame
    
        self.kamera.release()
        cv2.destroyAllWindows()