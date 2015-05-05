#!/usr/bin/python

import threading
import cv2
import StringIO
import time
import Image
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

class videoThread(threading.Thread):
    def __init__(self, cap):
        threading.Thread.__init__(self)
        global cam
        cam = cap
        self.cap = cap
   
    def run(self):
        server = HTTPServer(('', 8080), sendCap)
        server.serve_forever()
        
        
class sendCap(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('.mjpg'):
            self.send_response(200)
            self.send_header('Content-type', 'multipart/x-mixed-replace; boundary=--jpgboundary')
            self.end_headers()
            while True:
                ret, frame = cam.read()
                imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)    
                jpg = Image.fromarray(imgRGB)
                tmpFile = StringIO.StringIO()
                jpg.save(tmpFile, 'JPEG')
                self.wfile.write("--jpgboundary")
                self.send_header('Content-type', 'image/jpeg')
                self.send_header('Content-length', str(tmpFile.len))
                self.end_headers()
                jpg.save(self.wfile, 'JPEG')
                time.sleep(0.05)
                    
        elif self.path.endswith('.html'):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write('<html><head></head><body>')
            self.wfile.write('<img src="http://127.0.0.1:8080/cam.mjpg"/>')
            self.wfile.write('</body></html>')
            return
            
