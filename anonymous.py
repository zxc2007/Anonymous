#!/usr/bin/python
# -*- coding: utf-8 -*-
# Anonymous
# Coded by stepbystepexe
# Github: https://github.com/stepbystepexe/Anonymous

import os, sys, time, random, urllib, requests
import subprocess as sp
from time import sleep
from threading import Thread
from requests.exceptions import ConnectionError

info = """
Name        : Anonymous
Version     : 1.3 (Update: 31 March 2020, 1:10 AM)
Date        : 29 September 2019
Author      : Nedi Senja
Purpose     : Send a message to Anonymous
              anonymously.
Thankyou    : Allah SWT.
              FR13NDS, & all over
              humans on planet earth
NB          : Humans are not perfect
              as rich as this tool.
              Please report criticism or suggestions
              To - Email: d_q16x@outlook.co.id
                 - WhatsApp: tinyurl.com/wel4alo

[ \033[4mUse this tool wisely. Thanks \033[0m] """

example = """\033[0;44;77;1m[          Anonymous, My Github: @stepbystepexe          ]\033[0m"""

logo = """
 \033[0;31m█▀▀▀█ █▀▀▀█ █▀▀▀█ █▀▀▀█ █   █ █▀▀█▀▀█ █▀▀▀█ █   █ █▀▀▀▀
 \033[0;31m█▀▀▀█ █   █ █   █ █   █ ▀▀█▀▀ █  █  █ █   █ █   █ ▀▀▀▀█
 \033[0;31m▀   ▀ ▀   ▀ ▀▀▀▀▀ ▀   ▀   ▀   ▀     ▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀▀▀▀▀
"""

def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()

def play():
    animation = '|/-\\'
    for i in range(30):
        time.sleep(0.1)
        sys.stdout.write('\r\033[0m[\033[0;32m●\033[0m] Processing (' + animation[(i % len(animation))]+')')
        sys.stdout.flush()

def loads():
    o = [' .   ',' ..  ',' ... ']
    for i in o:
        print('\r\033[0m[\033[0;33m●\033[0m] Email sending'+i,end=''),;sys.stdout.flush();time.sleep(1)

def write(o):
    for i in o + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)

def sound():
    print()
    sp.call('mpv nada.o',shell=True,stdout=sp.DEVNULL,stderr=sp.STDOUT)
    print()
    restart()

def choose():
    print('\n')
    for i in random.choice(txt):
        print(str(i.replace('\n','')),end=''),;sys.stdout.flush();time.sleep(0.1)
    time.sleep(4)

def motto():
    global txt
    os.system('clear')
    os.system('reset')
    sleep(1)
    print()
    print(logo)
    print(example)
    print()
    txt = open('.___','r').readlines()
    st = ['\033[4;1mM O T T O\033[0m']
    for i in st:
        print(i.center(65))
    ttt = Thread(name='motto',target=sound)
    ttt.start()
    while ttt.is_alive():
        choose()

def anonim():
    os.system('clear')
    os.system('reset')
    sleep(1)
    print()
    print(logo)
    print(example)
    print()
    write("\033[0m[ \033[32mINFO \033[0m] \033[3mNever send an email to an illegal community")
    write("         that any risk is your responsibility")
    to = input('\n\n\033[0m[\033[101;77;1m   To    \033[0m] ')
    subject = input('\033[0m[\033[102;90;1m Subject \033[0m] ')
    message = input('\033[0m[\033[104;77;1m Message \033[0m] ')
    print()
    loads()
    try:
        user_agent = 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36'
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
            print()
            print("\033[0m[\033[1;96m+\033[0m] \033[1;77mSuccess send email !")
            print("\033[0m[\033[1;95m!\033[0m] \033[1;77mIn order to increase your privacy, the anonymous e-mail will be randomly delayed up to 12 hours")
            print()
    except requests.exceptions.ConnectionError:
        print('\n\n\033[0m[\033[91;1m!\033[0m] \033[77;1mNo connection \033[0m\n')
        sys.exit(1)

os.system('clear')
os.system('reset')
sleep(1)
print()
print(logo)
print(example)
print()
print("\033[0m[\033[96;2;1m1\033[0m] \033[1;77mSend Email Anonymous")
print("\033[0m[\033[96;2;1m2\033[0m] \033[1;77mMotto")
print()
print("\033[0m[\033[93;1m&\033[0m] LICENSE")
print("\033[0m[\033[94;1m#\033[0m] Information")
print("\033[0m[\033[92;1m*\033[0m] Update")
print("\033[0m[\033[91;1m-\033[0m] Exit")
print()
option = input("\033[0m(\033[105;77;1m/\033[0m) \033[1;77mChoose an option: \033[0m")
if option.strip() in '1 send'.split():
    print()
    play()
    sleep(1)
    anonim()
elif option.strip() in '2 motto'.split():
    print()
    play()
    sleep(1)
    motto()
elif option.strip() in '& 3 license'.split():
    print()
    os.system('nano LICENSE')
    print()
    restart()
elif option.strip() in '# 4 info'.split():
    os.system('clear')
    print(example)
    os.system('toilet -f smslant Anonim')
    print(info)
    sleep(1)
    print()
    input('[ Back ]')
    restart()
elif option.strip() in '* 5 update'.split():
    print()
    os.system('git pull origin master')
    print()
    input('\033[0m[ \033[32mBack \033[0m]')
    restart()
elif option.strip() in '- 0 exit'.split():
    print("\n\033[0m[\033[1;91m!\033[0m] \033[1;77mExit the program!")
    print()
    sys.exit(1)
else:
    print("\n\033[0m[=\033[1;41;77m Invalid Option \033[0m=]")
    print()
    sleep(1)
    restart()
