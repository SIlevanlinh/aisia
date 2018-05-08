from flask_restplus import Namespace, Resource, fields
from flask import Response
from ...utils.camera_util.camera_opencv import Camera
# from .camera_opencv import Camera

api = Namespace('video', description='Video related operations')

def gen(camera):
    """Video streaming generator function."""
    currentFrame = 0
    while True:
        frame = camera.get_frame()
        # name = './frames' + str(currentFrame) + '.jpg'
        # cv2.imwrite(name, frame)
        # currentFrame += 1
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@api.route('/')
class VideoFeed(Resource):
    def get(self):
        return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
