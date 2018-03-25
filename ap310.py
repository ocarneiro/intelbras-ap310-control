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

def changeLed(token, color, action):
    url = secrets.BASE_URL + 'cgi-bin/api/v1/service/leds'
    headers = {"content-type": "application/json", "authorization": "Bearer " + token}
    payload = {"data":{"active": True,
                       "color": {"value": color},
                       "action": {"value": action}
                      }
              }
    response = requests.request("PUT", url, data=json.dumps(payload), headers=headers, verify=False)
    return response

def apply(token):
    url = secrets.BASE_URL + 'cgi-bin/api/v1/system/apply'
    headers = {'authorization': 'Bearer ' + token}
    response = requests.request("POST", url, data="", headers=headers, verify=False)
    return response

if __name__ == '__main__':
    token = login()
    print(changeLed(token, "green", "on"))
    print(apply(token))