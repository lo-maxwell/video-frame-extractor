# source env/bin/activate
#python3 extracter.py

import cv2
import time
import os
import multiprocessing

global vidcap
movFile = '../sxf.mp4'
vidcap = cv2.VideoCapture(movFile)
#print('starting up cv2')

def extract_frame(frameNum):
    global vidcap
    #start2 = time.time()
    vidcap.set(1, frameNum)
    #print("set: " + str(time.time() - start2))
    success,image = vidcap.read()
    cv2.imwrite("sxf/frame%d.jpg" % frameNum, image)
    #print("write: " + str(time.time() - start2))

def main():
    path = 'sxf'
    movFile = '../sxf.mp4'

    global vidcap
    start = time.time()
    print("starting timer")
    #start2 = time.time()
    vidcap = cv2.VideoCapture(movFile)
    #print(time.time() - start2)
    #print(type(vidcap))
    numFrames = vidcap.get(7)
    print("file {0} has {1} frames".format(movFile, numFrames))


    print("setting up directory for path {0}".format(path))
    os.system("rm -rf {0}".format(path))
    os.system("mkdir {0}".format(path))

    cores = multiprocessing.cpu_count()
    print("setting up multiprocessing with {0} cores".format(cores))
    assert cores > 0, "Can't use {0} cpus!".format(cores)

    with multiprocessing.Pool(cores) as pool:
        pool.map(extract_frame, range(0,min(int(numFrames), 100)))

    end = time.time()
    print(end - start)
    f = open("sxf/stats.txt", "w")
    f.write("Total frames: \n{0}\nTime taken: \n{1}\n".format(numFrames, str(end - start)))
    f.close()

if __name__ ==  '__main__':
    main()
