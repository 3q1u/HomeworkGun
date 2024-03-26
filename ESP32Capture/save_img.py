import cv2
import numpy as np
import urllib.request

# Function to read the first frame from the ESP32-CAM and return it as an ndarray
def first_frame(stream_url):
    stream = urllib.request.urlopen(stream_url)
    bytes = b''
    while True:
        bytes += stream.read(1024)
        a = bytes.find(b'\xff\xd8')
        b = bytes.find(b'\xff\xd9')
        if a != -1 and b != -1:
            jpg = bytes[a:b+2]
            frame = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
            if frame is not None:
                return frame  # Return the frame as an ndarray

# URL of the video stream
stream_url = 'http://192.168.31.23/mjpeg/1'

# Read the first frame and store it as an ndarray
frame = first_frame(stream_url)
np.save('frame.npy', frame)
# Optionally display the frame
cv2.imshow('Frame', frame)
cv2.waitKey(0)  # Wait indefinitely until a key is pressed

# Clean up
cv2.destroyAllWindows()