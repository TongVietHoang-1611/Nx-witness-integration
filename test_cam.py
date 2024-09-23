import cv2

# Mở camera (thường là camera mặc định sẽ có chỉ số 0)
cap = cv2.VideoCapture(0)

# Kiểm tra xem có mở được camera không
if not cap.isOpened():
    print("Không thể mở camera")
    exit()

while True:
    # Đọc từng khung hình từ camera
    ret, frame = cap.read()

    # Nếu không thể đọc được khung hình thì thoát
    if not ret:
        print("Không thể nhận được khung hình")
        break

    # Hiển thị khung hình vừa đọc được
    cv2.imshow('Camera', frame)

    # Nhấn phím 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng camera và đóng tất cả các cửa sổ
cap.release()
cv2.destroyAllWindows()
