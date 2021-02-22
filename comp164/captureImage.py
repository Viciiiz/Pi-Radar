from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180
camera.start_preview()
sleep(3)
camera.capture('/var/www/html/comp164/image.jpg')
camera.stop_preview()
