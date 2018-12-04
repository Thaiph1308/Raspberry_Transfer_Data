import socket
import os
import glob
import json
import requests
import numpy as np
import time
import base64

PATH_TO_IMAGES = "Images"
url = "http://192.168.43.181:8080/fileupload"

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

def getserial_fake():
    cpuserial = "RASPID"
    return cpuserial

def change_directory(path):
    os.chdir(os.path.join(os.getcwd(),path))

def str_join(*args):
    return ''.join(map(str, args))


os.chdir(os.path.join(os.getcwd(),PATH_TO_IMAGES))
def send_image(path):
    print(os.getcwd())
    image_list =[]
    for i,image in enumerate(os.listdir(os.getcwd())):
        rename_image = getserial_fake() + "_" + str(i) + ".jpg"
        os.rename(image,rename_image)
        send_image_to_server(rename_image,url)
    return image_list

# change_directory(PATH_TO_IMAGES)
# images = find_image()
# cv2.imshow("Asdf",images[0])
# cv2.waitKey()
# print(images)
def send_image_to_server(image,url):
    #url = "http://192.168.43.181:8080/fileupload"
    filetoupload = {'filetoupload': open(str(image), 'rb')}
    r = requests.post(url, files=filetoupload)
    print(r.text)

if __name__ == '__main__':
    while True:
        #images = find_image()
        send_image(PATH_TO_IMAGES)
        print("Send image to server success")
        time.sleep(5)

