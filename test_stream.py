import requests
from requests.auth import HTTPDigestAuth

# Base URL and WebRTC endpoint
base_url = 'https://192.168.0.103:7001/'
webrtc_endpoint = 'webrtc/?camera_id=ee97298e-4f34-4c41-da78-4466f8ccac08'

# Authentication credentials

# Create a session to persist the authentication
session = requests.Session()

# Authenticate at the base URL with Digest Authentication
response = session.get("https://192.168.0.103:7001/rest/v2/login/users/admin?_format=JSON&_keepDefault=true&_pretty=true", verify=False)
print(response)
# Check if the authentication is successful
if response.status_code == 200:
    print("Authentication successful!")
    
    # After successful authentication, access the WebRTC endpoint
    webrtc_url = base_url + webrtc_endpoint
    print(webrtc_url)
    
    # Use the same session to access the WebRTC URL
    webrtc_response = session.get(webrtc_url, verify=False)
    
    # Check if the WebRTC request is successful
    if webrtc_response.status_code == 200:
        with open('output.mp4', 'wb') as file:
            file.write(webrtc_response.content)
        print("Video saved as 'output.mp4'")
    else:
        print(f"Error accessing WebRTC endpoint: {webrtc_response.status_code}")
else:
    print(f"Authentication failed with status code: {response.status_code}")
