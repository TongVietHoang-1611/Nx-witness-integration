import requests
import av
from requests.auth import HTTPDigestAuth
from io import BytesIO

def check_webm_stream_contents(url, username, password):
    # Tạo một phiên requests với xác thực
    session = requests.Session()
    session.auth = (username, password)

    # Mở stream
    response = session.get(url, auth=HTTPDigestAuth(username, password), stream=True, verify=False)

    if response.status_code != 200:
        print(f"Không thể kết nối. Mã trạng thái: {response.status_code}")
        return

    print("Đã kết nối thành công")

    # Tạo một buffer để lưu trữ dữ liệu stream
    buffer = BytesIO()

    try:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                buffer.write(chunk)
                buffer.seek(0)

                # Sử dụng av để đọc và giải mã WebM stream
                try:
                    with av.open(buffer) as container:
                        print(f"Tệp WebM này chứa {len(container.streams)} stream(s):")
                        
                        for stream in container.streams:
                            print(f"Stream {stream.index}:")
                            print(f"  Loại: {stream.type}")
                            if stream.type == 'video':
                                print(f"  Độ phân giải: {stream.width}x{stream.height}")
                                print(f"  Tỉ lệ khung hình: {stream.average_rate}")
                            elif stream.type == 'audio':
                                print(f"  Kênh âm thanh: {stream.channels}")
                                print(f"  Tần số mẫu: {stream.sample_rate}")

                        # Sau khi hiển thị thông tin, dừng lại
                        return

                except av.AVError as e:
                    print(f"Lỗi giải mã: {e}")
                    return

    finally:
        buffer.seek(0)
        buffer.truncate()

# Thông tin kết nối
url = "http://192.168.0.73:7001/media/ee97298e-4f34-4c41-da78-4466f8ccac08.webm"
username = "admin"
password = "Hoang1234"

# Gọi hàm kiểm tra nội dung WebM
check_webm_stream_contents(url, username, password)
