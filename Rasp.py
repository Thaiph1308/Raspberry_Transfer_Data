import socket
import os
import glob
from PIL import Image
import json
import cv2 
import numpy as np
import time
import base64

PATH_TO_IMAGES = "Images"

def getIP():
    try:
        myip = ((([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0])
        return myip
    except :
        return ''

def getserial():
# Extract serial from cpuinfo file
    cpuserial = "0000000000000000"
    try:
        f = open('/proc/cpuinfo','r')
        for line in f:
            if line[0:6]=='Serial':
                cpuserial = line[10:26]
        f.close()
    except:
        cpuserial = "Can not found CPU ID, ERROR000000000"
    return cpuserial
def change_directory(path):
    os.chdir(os.path.join(os.getcwd(),path))

def find_image():
    print(os.getcwd())
    image_list =[]
    for image in glob.glob("*.jpg"):
        im = cv2.imread(image)
        print(type(im))
        image_list.append(im)
    return image_list

change_directory(PATH_TO_IMAGES)
images = find_image()
cv2.imshow("Asdf",images[0])
cv2.waitKey()
print(images)

def create_json(image):
    #data = Image.open(image)
    data=image
    print(data)
    outjson = {}
    outjson['image'] = data   # data has to be encoded base64 and decode back in the Android app base64 as well
    outjson['DeivceID'] = getserial()
    json_data = json.dumps(outjson)
    print(json_data)
    return json_data

# if __name__ == '__main__':
#     while True:
#         images = find_image()
#         print("HELLO")
#         time.sleep(5)

