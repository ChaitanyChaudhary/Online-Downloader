# Online Downloader

import requests
from tqdm import tqdm
import os
from urllib.parse import urlparse

# User Input
url = input("Enter The File URL: ")

# Extract URL Name For File Name
filename = os.path.basename(url)

r = requests.get(url, stream=True)
totalExpectedBytes = int(r.headers["Content-Length"])
# print(totalExpectedBytes)
bytesReceived = 0
progress_bar = tqdm(total=totalExpectedBytes, unit='iB', unit_scale=True)

with open(f'{filename}', 'wb') as f:
    for chunk in r.iter_content(chunk_size=128):
        # print(f"{bytesReceived} received out of total {totalExpectedBytes}")
        progress_bar.update(128)
        f.write(chunk)
        bytesReceived += 128
progress_bar.close()