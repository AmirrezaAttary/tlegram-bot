# import os
# import requests

# dump_directory = os.path.join(os.getcwd(), 'mp3')
# os.makedirs(dump_directory, exist_ok=True)


# def dump_mp3_for(resource):
#     payload = {
#         'api': 'advanced',
#         'format': 'JSON',
#         'video': resource
#     }
#     initial_request = requests.get('http://youtubeinmp3.com/fetch/', params=payload)
#     if initial_request.status_code == 200:  # good to go
#         download_mp3_at(initial_request)


# def download_mp3_at(initial_request):
#     j = initial_request.json()
#     filename = '{0}.mp3'.format(j['title'])
#     r = requests.get(j['link'], stream=True)
#     with open(os.path.join(dump_directory, filename), 'wb') as f:
#         print('Dumping "{0}"...'.format(filename))
#         for chunk in r.iter_content(chunk_size=1024):
#             if chunk:
#                 f.write(chunk)
#                 f.flush()


import requests

# URL of the video
# video_url = 'https://persian11.asset.aparat.com/aparat-video/ebfaf62f2f6c5341a73b374dddd92d7c59284641-144p.mp4?wmsAuthSign=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6ImRmZmYzNjc5NzlmODc1ODQ0Njg4N2NlMWJhODU5ZTUwIiwiZXhwIjoxNzQwNDk2MzIzLCJpc3MiOiJTYWJhIElkZWEgR1NJRyJ9.mwAkW4chCMwmri4GeahCmur5e57gpjQYcb_ge_m5BmM'
video_url = ['https://www.aparat.com/api/fa/v1/video/video/show/videohash']
params = {
    'pr'
}
# Get the video content
response = requests.get(video_url, stream=True)

# Check if the request was successful
if response.status_code == 200:
    # Open a local file in binary write mode
    with open('downloaded_video.mp4', 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024*1024):  # Download in 1 MB chunks
            if chunk:  # filter out keep-alive new chunks
                file.write(chunk)
else:
    print(f'Failed to retrieve video: status code {response.status_code}')