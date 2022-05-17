# source env/bin/activate
#python3 extracter.py

import cv2
import time
import os

path = "sxf"
print("setting up directory for path {0}".format(path))
os.system("rm -rf {0}".format(path))
os.system("mkdir {0}".format(path))

start = time.time()
print("starting timer")
vidcap = cv2.VideoCapture('../sxf.mp4')
success,image = vidcap.read()
count = 0
while count < 100 and success:
  cv2.imwrite("sxf/frame%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  # print('Read a new frame: ', str(count) if success else 'ERROR')
  count += 1


end = time.time()
print(end - start)
f = open("sxf/stats.txt", "w")
f.write("Total frames: \n{0}\nTime taken: \n{1}\n".format(count, str(end - start)))
f.close()
