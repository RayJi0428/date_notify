import os
import requests
import codecs
import json
from bs4 import BeautifulSoup

# -------------------------------------------------------------------------------------------
line_notify_url = "https://notify-api.line.me/api/notify"
line_header = {}
# -------------------------------------------------------------------------------------------
# 發送Line訊息


def setToken(token):
    global line_header
    line_header = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }


def sendMessage(msg):
    # function docstring
    line_notify_url = "https://notify-api.line.me/api/notify"
    payload = {'message': msg}
    req_line = requests.post(
        line_notify_url, headers=line_header, params=payload)
    return req_line.status_code

# -------------------------------------------------------------------------------------------
# 發送Line圖片


def sendImage(imageURL):
    # function docstring
    payload = {'message': imageURL, 'imageThumbnail': imageURL,
               'imageFullsize': imageURL}
    req_line = requests.post(
        line_notify_url, headers=line_header, params=payload)
    return req_line.status_code
