from primesense import openni2
import cv2
import numpy as np

openni2.initialize()     # can also accept the path of the OpenNI redistribution

dev = openni2.Device.open_any()
print dev.get_device_info()

depth_stream = dev.create_depth_stream()
depth_stream.start()
#**********************#

def get_depth():
    dmap = np.fromstring(depth_stream.read_frame().get_buffer_as_uint8(), dtype=np.uint8)
    dmap = dmap.reshape(800, 768)  # Works & It's FAST
    #print type(dmap)
    d4d = np.uint8(dmap.astype(float)) #* 255/ 2**12 -1) # Correct the range. Depth images are 12bits
    #d4d = cv2.cvtColor(d4d,cv2.COLOR_GRAY2RGB)
    #print type(d4d)
    # Shown unknowns in black
    #d4d = 255 - d4d    
    return dmap, d4d

while cv2.waitKey(1) != 27:
    dmap, d4d= get_depth()
    cv2.imshow('Depth', dmap)
    continue

cv2.destroyAllWindows()
depth_stream.stop()
openni2.unload()