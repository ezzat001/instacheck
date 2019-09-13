import requests
import json
from random import randint
from bs4 import BeautifulSoup

""" emailOrPhone
    fullName
    username
    password
    coreSpriteInputError
    coreSpriteInputAccepted
"""
EMAIL = str(input('Email:'))
def reset(email):
    BASE_URL = 'https://instagram.com'
    REGISTER_URL = BASE_URL+'/accounts/emailsignup/'

    USER_AGENT= 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.364 (KHTML, like Gecko)\
        Chrome/59.0.3071.115 Safari/537.6'
    session = requests.Session()
    session.headers = {'user-agent': USER_AGENT}
    session.headers.update({'Referer': BASE_URL})

    req = session.get(BASE_URL)
    session.headers.update({'x-CSRFToken': req.cookies['csrftoken']})
    register_data = {'emailOrPhone': EMAIL, 'fullName': 'User'+str(randint(100,999)),
                     'username': 'asdfasxkems1692', 'password' : '123'}
    session.headers.update({'Referer': REGISTER_URL})
    register = session.post(REGISTER_URL, data=register_data, allow_redirects=True)
    session.headers.update({'X-CSRFToken': register.cookies['csrftoken']})
    cookies = register.cookies
    #x = session.get(REGISTER_URL)
    response_text = BeautifulSoup(register.content)
    return response_text

y = reset('fuckasagag123123123xsjajsaa.com')

print(y)


