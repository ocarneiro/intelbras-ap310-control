# coding: utf-8
import requests
import json
import secrets

def login():
    data = {'data':{'username':secrets.usuario,'password':secrets.senha}}
    url = secrets.BASE_URL + 'cgi-bin/api/v1/system/login'
    response = requests.post(url,data=json.dumps(data),verify=False)
    token = json.loads(response.content.decode('utf-8'))['data']['Token']
    return token

print(login())