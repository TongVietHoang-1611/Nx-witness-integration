import cv2
import mediapipe as mp
from flask import Flask, Response, render_template

# Khởi tạo Flask
app = Flask(__name__)

# Khởi tạo MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
rtsp_url = 'rtsp://admin:Hoang1234@192.169.1.18:7001/0ca6d03e-adaf-bfbf-38f7-c5d563001e45'
# Mở camera
cap = cv2.VideoCapture(1)

def generate_frames():
    # Khởi tạo đối tượng Face Detection
    with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
        while True:
            # Đọc khung hình từ camera
            ret, frame = cap.read()
            if not ret:
                break

            # Chuyển đổi khung hình từ BGR sang RGB để xử lý
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Phát hiện khuôn mặt
            results = face_detection.process(frame_rgb)

            # Nếu tìm thấy khuôn mặt, vẽ hộp quanh mặt
            if results.detections:
                for detection in results.detections:
                    mp_drawing.draw_detection(frame, detection)

            # Chuyển khung hình thành định dạng JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Trả về khung hình dưới dạng một luồng video
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# Route chính để render template
@app.route('/')
def index():
    return render_template('index.html')

# Route để stream video
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
