#!/data/data/com.termux/files/usr/bin/python
# -*- coding: utf-8 -*-
# Anonymous
# Coded by Senja
# Github: https://github.com/stepbystepexe/Anonymous
from __opt__ import *
import os, sys, time, random, requests, marshal
def loads():
    tix = [
     '.   ', '..  ', '... ']
    for o in tix:
        print '\r\x1b[0m[\x1b[94;1m\xe2\x97\x8f\x1b[0m] \x1b[0mSending ' + o,
        sys.stdout.flush()
        time.sleep(1)
os.system('clear')
os.system('reset')
time.sleep(1)
print
print(logo)
print("\033[0;44;1;77m[       Anonymous Email v1.0, Coded by @stepbystep       ]\033[0m")
print
to = raw_input('\033[0m[\033[1;91m-\033[0m] \033[1;77mTo: \033[0m')
subject = raw_input('\033[0m[\033[1;92m#\033[0m] \033[1;77mSubject: \033[0m')
message = raw_input('\033[0m[\033[1;93m*\033[0m] \033[1;77mmessage: \033[0m')
loads()
user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
sess = requests.Session()
email_req = sess.post('http://anonymouse.org/cgi-bin/anon-email.cgi', headers={
        'Host': 'anonymouse.org',
        'User-Agent': user_agent,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://anonymouse.org/anonemail.html',
        'Connection': 'close',
        'Upgrade-Insecure-Requests':'1',
        'Content-Type':'application/x-www-form-urlencoded'
}, data={
        'to': to,
        'subject': subject,
        'text': message
})
if 'The e-mail has been sent' in email_req.text:
    os.system('xdg-open https://github.com/stepbystepexe')
    print
    print("\033[0m[\033[1;96m+\033[0m] \033[1;77mEmail Sent!")
    print("\033[0m[\033[1;95m!\033[0m] \033[1;77mIn order to increase your privacy, the anonymous e-mail will be randomly delayed up to 12 hours")
    print
