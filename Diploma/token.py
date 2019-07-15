# -*- coding: utf-8 -*-
app_id = 7058222
app_token = 'R1hGw79znxTrb0HhWnxC'
import requests


params = {
        'client_id': app_id,
        'scope': 'friends,offline',
        'redirect_uri': 'https://oauth.vk.com/blank.html',
        'display': 'page',
        'v': 5.101,
        'response_type': 'token'
        }

url = 'https://oauth.vk.com/authorize'

response = requests.get(url, params=params)
print(response.text)