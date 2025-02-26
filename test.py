import requests

def fech(url):
    video_url = f'https://www.aparat.com/api/fa/v1/video/video/show/videohash/{url}'
    res = requests.get(video_url)
    return res.json()

fech("khg28i5")


def send_welcome(message):
    