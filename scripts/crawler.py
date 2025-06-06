#!/usr/bin/python3
# crawler.py: get posts from bsky.com
# usage: crawler.py
# 202241123 erikt(at)xs4all.nl


import datetime
import json
import os
import requests
import regex
import time


LOCAL_DIR = "/home/erikt/software/bsky"
URL = "https://api.bsky.app/xrpc/app.bsky.feed.searchPosts"
# 20241226 10:50 added: ik is in je maar die ook wat dan nog om dit
QUERY_WORDS = ["aan",
               "als",
               "bij", "dan",
               "dat",
               "de", "die", "dit",
               "een",
               "en",
               "er",
               "geen",
               "het", "ik", "in", "is", "je", "maar",
               "met",
               "niet", "nog", "om", "ook",
               "op",
               "te",
               "van",
               "voor", "wat",
               "wel",
               "ze",
               "zijn",
               "zo"]


def save_posts(query, json_data):
    file_name = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S") + "-" + query + ".json"
    with open(file_name, 'w') as out_file:
       json.dump(json_data, out_file)
       out_file.close


def get_posts(query, lang="nl"):
    params = {"q": query, "lang": lang, "limit": 100}
    response = requests.get(URL, params=params)
    if response.status_code == 200:
        json_data = response.json()
        save_posts(query, json_data)
        return json_data
    else:
        print(f"Error: {response.status_code}")


os.chdir(LOCAL_DIR)
for word in QUERY_WORDS:
    get_posts(word)
    time.sleep(1)


exit(0)
