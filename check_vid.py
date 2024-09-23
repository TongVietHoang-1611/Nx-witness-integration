import requests
from requests.auth import HTTPDigestAuth

def check_stream_format(url, username, password):
    session = requests.Session()
    session.auth = (username, password)

    response = session.get(url, auth=HTTPDigestAuth(username, password), stream=True, verify=False)

    if response.status_code != 200:
        print(f"Không thể kết nối. Mã trạng thái: {response.status_code}")
        return

    print("Headers của response:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")

    print("\nKiểm tra nội dung stream:")
    content_type = response.headers.get('Content-Type', '')
    print(f"Content-Type: {content_type}")

    # Đọc một số byte đầu tiên của stream
    initial_bytes = response.raw.read(1024)
    print(f"\n{len(initial_bytes)} byte đầu tiên (hex):")
    print(initial_bytes.hex())

    # Kiểm tra các signature phổ biến
    if initial_bytes.startswith(b'\x00\x00\x00\x1cftypisom'):
        print("Có thể là một MP4 stream")
    elif initial_bytes.startswith(b'\x1aE\xdf\xa3'):
        print("Có thể là một WebM stream")
    elif initial_bytes.startswith(b'\xff\xd8'):
        print("Có thể là một MJPEG stream")
    else:
        print("Không thể xác định định dạng từ các byte đầu tiên")

# Thông tin kết nối
url = "http://192.168.0.73:7001/media/ee97298e-4f34-4c41-da78-4466f8ccac08.webm"
username = "admin"
password = "Hoang1234"

check_stream_format(url, username, password)