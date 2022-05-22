import cv2
from flask import Flask, render_template, Response
from time import time

app = Flask('__name__')

video = cv2.VideoCapture(0)


def video_stream():
    # Visualization parameters
    row_size = 40  # pixels
    left_margin = 24  # pixels
    text_color = (255, 255, 255)  # white
    font_size = 2
    font_thickness = 1
    fps_avg_frame_count = 10

    # Variables to calculate FPS
    counter, fps = 0, 0
    start_time = time()

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_eye.xml')

    while True:
        ret, frame = video.read()
        if not ret:
            print('no image - breaking')
            break
        else:
            # Calculate the FPS
            counter += 1
            if counter % fps_avg_frame_count == 0:
                end_time = time()
                fps = fps_avg_frame_count / (end_time - start_time)
                start_time = time()

            # Show the FPS
            fps_text = 'FPS = {:.1f}'.format(fps)
            text_location = (left_margin, row_size)
            print(fps_text)
            cv2.putText(frame, fps_text, text_location, cv2.FONT_HERSHEY_PLAIN,
                        font_size, text_color, font_thickness)

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
                roi_gray = gray[y:y+w, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey),
                                  (ex + ew, ey + eh), (0, 255, 0), 5)

            ret, buffer = cv2.imencode('.jpeg', frame)
            frame = buffer.tobytes()
            yield (b' --frame\r\n' b'Content-type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def camera():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(video_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')


app.run(host='0.0.0.0', port='5000', debug=False)
