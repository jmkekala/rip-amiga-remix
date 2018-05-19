#!/usr/bin/python3.6
''' This script will download songs of the amigaremix.com page'''

import time
import re
import urllib
import urllib.request
from pathlib import Path
from bs4 import BeautifulSoup



PAGES = list(range(1, 33))

for page in PAGES:
    url = 'http://amigaremix.com/remixes/' + str(page)
    print(url)
    time.sleep(0.1)

    htmlfile = urllib.request.urlopen(url)
    soup = BeautifulSoup(htmlfile, 'html.parser')

    for link in soup.find_all('a', 'remix'):
        if not 'html' in link.get('href'):
            song_url = "http://amigaremix.com" + str(link.get('href'))
            song_name = (re.sub(r'^/listen/[0-9]*/', '', str(link.get('href'))))
            song_name = (re.sub(r'%20-%20', ' - ', song_name))

            song_destination = 'music/' + str(song_name)
            if not Path(song_destination).is_file():
                try:
                    urllib.request.urlretrieve(song_url, song_destination)
                except:
                    print (song_url)
