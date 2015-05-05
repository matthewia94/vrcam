#/usr/bin/env python
import threading
import serial
import cv2
import SocketServer
from videoThread import videoThread
from UDPHandler import UDPHandler 

__author__ = "Matt Anderson"

#Open serial communication with arduino
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1);
HOST, PORT = "localhost", 9999

def init(): 
    #OpenCV setup
    cam = cv2.VideoCapture(0)
    camThread = videoThread(cam)
    camThread.daemon = True
    camThread.start()
    
    sockSer = SocketServer.UDPServer((HOST, PORT), UDPHandler)
    sockThread = threading.Thread(target=sockSer.serve_forever)
    sockThread.daemon = True
    sockThread.start()
    
    
def exit():
    ser.close()
    camThread.stop()
    sockThread.stop()
    

if __name__ == "__main__":
    init() 

    command = ''
    while command != 'exit':
        command = raw_input('command: ') 
        if command != 'exit':
            ser.write(command)
    
    exit()
