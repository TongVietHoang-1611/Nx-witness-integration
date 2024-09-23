import cv2

# Đường dẫn RTSP (thay thế bằng đường dẫn RTSP của bạn)
rtsp_url = 'rtsp://admin:Hoang1234@192.169.1.18:7001/0ca6d03e-adaf-bfbf-38f7-c5d563001e45'

# Mở kết nối tới luồng RTSP
cap = cv2.VideoCapture(rtsp_url)

# Kiểm tra xem kết nối có thành công không
if not cap.isOpened():
    print("Không thể kết nối đến luồng RTSP")
else:
    print("Kết nối thành công. Bắt đầu hiển thị...")

# Hiển thị luồng video
while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        print("Không thể nhận frame (kết thúc luồng RTSP)")
        break

    # Hiển thị frame nhận được
    cv2.imshow('RTSP Stream', frame)
    
    # Nhấn 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()
