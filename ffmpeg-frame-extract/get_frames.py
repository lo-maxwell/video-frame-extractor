import argparse
import FFMPEGFrames
import time

start = time.time()
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True)
ap.add_argument("-f", "--fps", required=True)
args = vars(ap.parse_args())

input = args["input"]
fps = args["fps"]

f = FFMPEGFrames.FFMPEGFrames("data/images/")
f.extract_frames(input, fps)

end = time.time()
print("time taken: " + str(end - start))
f = open("stats.txt", 'w')
f.write("Time taken: {0}".format(str(end-start)))
f.close()

