# import requests

# # URL of the video
# video_url = 'https://caspian18.asset.aparat.com/aparat-video/f835dd55288267e29eca1b6105ea510262307670-144p.mp4?wmsAuthSign=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6ImYzMDYwOWUyNDFiYjU5NTRjMWRkNGY4M2M0MzhlNTc2IiwiZXhwIjoxNzQwNjU3NTQzLCJpc3MiOiJTYWJhIElkZWEgR1NJRyJ9.IDKtIY9LJtEw9fbJcPagJFdhqypDe8ex79KxzVmd56g'

# # Get the video content
# response = requests.get(video_url, stream=True)

# # Check if the request was successful
# if response.status_code == 200:
#     # Open a local file in binary write mode
#     with open('downloaded_video.mp4', 'wb') as file:
#         for chunk in response.iter_content(chunk_size=1024*1024):  # Download in 1 MB chunks
#             if chunk:  # filter out keep-alive new chunks
#                 file.write(chunk)
# else:
#     print(f'Failed to retrieve video: status code {response.status_code}')


import re

text = "https://www.aparat.com/v/iab235w"
pattern = r"aparat\.com/v/([a-zA-Z0-9]+)"

match = re.search(pattern, text)
if match:
    video_id = match.group(1)
    print(video_id)