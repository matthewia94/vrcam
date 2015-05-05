#!/usr/bin/python

import threading
import cv2
import StringIO
import time

class videoThread(threading.Thread):
   def __init__(self, cap):
       threading.Thread.__init__(self)
       self.cap = cap
   
   def run(self):
       while(True):
           ret, frame = self.cap.read()
           imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)         
           cv2.imshow('frame', frame)
           if cv2.waitKey(1) & 0xFF == ord('q'):
               break
       
       cap.release()
       cv2.destroyAllWindows()
