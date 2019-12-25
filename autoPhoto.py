from time import sleep
from picamera import PiCamera

import time
nowtime = time.strftime("%Y_%m_%d_%H:%M:%S",time.localtime())

import requests

def lineNotifyMessage(token, picURI):
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    files = {'imageFile': open(picURI, 'rb')}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, files = files)
    return r.status_code

# 修改為你要傳送的訊息內容
message = 'take a Selfie'
# 修改為你的權杖內容
token = '1RyOE1jpJNxtgMWSve7VT2nOiTj0kyxmnuq5T4wiOet'



camera = PiCamera(resolution=(1920,1080)), framerate=30)
# Set ISO to the desired value
camera.iso = 100
# Wait for the automatic gain control to settle
sleep(2)
# Now fix the values
camera.shutter_speed = camera.exposure_speed
camera.exposure_mode = 'off'
g = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = g
# Finally, take several photos with the fixed settings

picName = nowtime+'.jpg'
camera.capture(picName)

picURI = picName
lineNotifyMessage(token, message)
