import os
import subprocess

# p1 = subprocess.run(["cat","test.txt"],capture_output=True, text=True)

# print(p1.stdout)

subprocess.call(['./darknet', 'detect', 'cfg/yolov3.cfg', 'yolov3.weights', 'data/dog.jpg'], shell=True)