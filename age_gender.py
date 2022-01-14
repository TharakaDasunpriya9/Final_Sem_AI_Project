from flask import Flask, render_template, Response
from camera import Video

age_gender=Flask(__name__)

@age_gender.route('/')
def index():
    return render_template('detection.html')

def gen(camera):
    while True:
        frame=camera.get_frame()
        yield(b'--frame\r\n'
       b'Content-Type:  image/jpeg\r\n\r\n' + frame +
         b'\r\n\r\n')

@age_gender.route('/video')

def video():
    return Response(gen(Video()),
    mimetype='multipart/x-mixed-replace; boundary=frame')

age_gender.run(debug=True,port=5002)