import cv2
from .base_camera import BaseCamera
import os

class Camera(BaseCamera):
    video_source = 0

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def frames():
        camera = cv2.VideoCapture(Camera.video_source)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        count = 0
        while True:
            # read current frame
            _, img = camera.read()

            # dirname = os.path.dirname(__file__)
            # output_dir = os.path.join(dirname, 'frames')
            # if count%100 == 0 :
            #     cv2.imwrite(output_dir + '/frame%d.jpg'%count,img)
            #     print(output_dir + '/frame')
            # count+=1

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()
