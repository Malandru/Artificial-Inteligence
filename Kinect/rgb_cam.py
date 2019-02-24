import numpy as np
import cv2
from primesense import openni2#, nite2
#from primesense import _openni2 as c_api

## Initialize openni and check
dist ='/opt/OpenNI/OpenNI-Linux-x64-2.2/Redist'
openni2.initialize(dist) #
if (openni2.is_initialized()):
    print "openNI2 initialized"
else:
    print "openNI2 not initialized"


## Register the device
dev = openni2.Device.open_any()
## Create the streams stream

rgb_stream = dev.create_color_stream()
## Check and configure the depth_stream -- set automatically based on bus speed
print 'The rgb video mode is', rgb_stream.get_video_mode() # Checks rgb video configuration
#rgb_stream.set_video_mode(c_api.OniVideoMode(pixelFormat=c_api.OniPixelFormat.ONI_PIXEL_FORMAT_RGB888, resolutionX=320, resolutionY=240, fps=30))
## Start the streams
rgb_stream.start()

def get_rgb():
    bgr   = np.fromstring(rgb_stream.read_frame().get_buffer_as_uint8(), dtype=np.uint8).reshape(640,480,3)
    rgb   = cv2.cvtColor(bgr,cv2.COLOR_BGR2RGB)
    return rgb
#get_rgb


## main loop

s=0
done = False

while not done:
    key = cv2.waitKey(1) & 255
    ## Read keystrokes
    if key == 27: # terminate
        print "\tESC key detected!"
        done = True

    elif chr(key) =='s': #screen capture
        print "\ts key detected. Saving image {}".format(s)
        cv2.imwrite("ex2_"+str(s)+'.png', rgb)
    rgb = get_rgb()
    cv2.imshow('rgb', rgb)


## Release resources 
cv2.destroyAllWindows()
rgb_stream.stop()
openni2.unload()

print ("Terminated")