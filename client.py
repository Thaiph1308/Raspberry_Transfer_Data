import requests
url = "http://192.168.43.181:8080/fileupload"
filetoupload = {'filetoupload': open('bxx.jpg', 'rb')}
print(type(filetoupload))
r = requests.post(url, files=filetoupload)
print(r.text)