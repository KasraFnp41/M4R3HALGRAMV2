import os
import requests
from time import sleep
import re
from json import loads
import colorama
from colorama import Fore
import requests,uuid,secrets
print(Fore.GREEN + """
███╗   ███╗  ██╗██╗██████╗ ██████╗ ██╗  ██╗ █████╗ ██╗ 
████╗ ████║ ██╔╝██║██╔══██╗╚════██╗██║  ██║██╔══██╗██║
██╔████╔██║██╔╝ ██║██████╔╝ █████╔╝███████║███████║██║
██║╚██╔╝██║███████║██╔══██╗ ╚═══██╗██╔══██║██╔══██║██║
██║ ╚═╝ ██║╚════██║██║  ██║██████╔╝██║  ██║██║  ██║███████╗
╚═╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝

[✒] Maded By : @m4r3hal""")                                     
 
from time import sleep
uid = uuid.uuid4()
 
 
 
 
r = requests.Session()
cookie = secrets.token_hex(8)*2
username = input(Fore.GREEN + '[-] IG Username : ')
password = input(Fore.GREEN + '[-] IG Password : ')
target = input(Fore.GREEN + '[-] IG Target ID : ')
sle = int(input(Fore.GREEN + '[-] Report Cooldown : '))
def login():
    global username
    global password
    url = 'https://www.instagram.com/accounts/login/ajax/'
    headers = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36', 'x-csrftoken': 'missing', 'mid': cookie}
    data = {'username':username,
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
            'queryParams': '{}',
            'optIntoOneTap': 'false',}
    req_login = r.post(url,headers=headers,data=data)
    if ("userId") in req_login.text:
        r.headers.update({'X-CSRFToken': req_login.cookies['csrftoken']})
        print(Fore.GREEN + '[✔] Login Successfully')
        url_id = 'https://www.instagram.com/{}/?__a=1'.format(target)
        req_id = r.get(url_id).json()
        user_id = str(req_id['logging_page_id'])
        idd = user_id.split('_')[1]
        done = 1
        while True:
            url_report = 'https://www.instagram.com/users/{}/report/'.format(idd)
            datas = {'source_name':'','reason_id':4,'frx_context':''} #spam
            report = r.post(url_report,data=datas)
            print(Fore.GREEN + '[+] Spam Done : {}'.format(done))
            sleep(sle)
            done += 1
    else:
        print(Fore.RED + '[x] Login Failed')
        exit()
 
login()