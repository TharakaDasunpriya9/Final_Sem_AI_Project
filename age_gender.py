from flask import Flask, render_template, Response
from camera import Video

application= Flask(__name__)
@application.route('/age_gender')
def age_gender():
    return render_template('detection.html')

def gen(camera):
    while True:
        frame=camera.get_frame()
        yield(b'--frame\r\n'
       b'Content-Type:  image/jpeg\r\n\r\n' + frame +
         b'\r\n\r\n')

@application.route('/video')
def video():
    return Response(gen(Video()),
    mimetype='multipart/x-mixed-replace; boundary=frame')

