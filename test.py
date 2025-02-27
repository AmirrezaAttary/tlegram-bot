import requests as RQ
import os
import re

if not os.path.exists("downloads"):
    os.makedirs("downloads")



def download_file(url):
    response = RQ.get(url, stream=True)

    # Check if the request was successful
    if response.status_code == 200:
        # Open a local file in binary write mode
        with open('downloaded_video.mp4', 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024*1024):  # Download in 1 MB chunks
                if chunk:  # filter out keep-alive new chunks
                    file.write(chunk)
    else:
        print(f'Failed to retrieve video: status code {response.status_code}')



def feth(text_query):
    url = f'https://www.aparat.com/api/fa/v1/video/video/show/videohash/{text_query}'
    respanse = RQ.get(url=url)
    res_js = respanse.json()['data']["attributes"]["file_link_all"]
    for item in res_js:
        if item['profile'] == '144p':
            urls_string = item.get('urls')
            for urls in urls_string:
                download_file(urls)


def re_text_input(url):
    text = url
    pattern = r"aparat\.com/v/([a-zA-Z0-9]+)"

    match = re.search(pattern, text)
    if match:
        video_id = match.group(1)
        feth(video_id)


re_text_input("https://www.aparat.com/v/qbe8s9g")