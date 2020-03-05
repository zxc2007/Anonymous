#!/usr/bin/python
# -*- coding: utf-8 -*-
# Anonymous
# Coded by Nedi Senja
# Github: https://github.com/stepbystepexe/Anonymous

import os, sys, time, random, requests, urllib3
import subprocess as sp
from time import sleep
from threading import Thread
from requests.exceptions import ConnectionError

info = """
Nama        : Anonymous
Versi       : 3.0 (Update: 12 Juli 2020, 1:00 AM)
Tanggal     : 01 Januari 2019
Author      : Nedi Senja
Tujuan      : Mengirim pesan kepad Anonymous
              secara anonim
Terimakasih : Allah SWT.
              FR13NDS, & seluruh
              manusia seplanet bumi
NB          : Manusia gax ada yang sempurna
              sama kaya tool ini.
              Silahkan laporkan kritik atau saran
              Ke - Email: d_q16x@outlook.co.id
                 - WhatsApp: +62 8577-5433-901

[ \033[4mGunakan tool ini dengan bijak \033[0m]\n """

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

def loads():
    o = [' .   ',' ..  ',' ... ']
    for i in o:
        print('\r\033[0m[\033[0;33m●\033[0m] Sedang mengirim'+i,end=''),;sys.stdout.flush();time.sleep(1)

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

def choic():
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
    while ttt.isAlive():
            choic()

def anonim():
    os.system('clear')
    os.system('reset')
    sleep(1)
    print()
    print(logo)
    print(example)
    print()
    write("\033[0m[ \033[32mINFO \033[0m] \033[3mJangan pernah anda mengirim Email pada Komunitas")
    write("         Ilegal segala resiko menjadi tanggung jawab Anda")
    to = input('\n\n\033[0m[\033[101;77;1m Kepada \033[0m] ')
    subject = input('\033[0m[\033[102;90;1m Subjek \033[0m] ')
    message = input('\033[0m[\033[104;77;1m Pessan \033[0m] ')
    print()
    loads()
    try:
        user_agent = 'Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.4 Chrome/67.0.3396.87 Mobile Safari/537.36'
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
            print("\033[0m[\033[1;96m+\033[0m] \033[1;77mEmail terkirim sukses !")
            print("\033[0m[\033[1;95m!\033[0m] \033[1;77mIn order to increase your privacy, the anonymous e-mail will be randomly delayed up to 12 hours")
            print()
    except requests.exceptions.ConnectionError:
        print('\n\n\033[0m[\033[91;1m!\033[0m] \033[77;1mTidak ada koneksi\033[0m\n')
        sys.exit(1)

os.system('clear')
os.system('reset')
sleep(1)
print()
print(logo)
print(example)
print()
print("\033[0m[\033[96;2;1m1\033[0m] \033[1;77mKirim Email Anonim")
print("\033[0m[\033[96;2;1m2\033[0m] \033[1;77mMotto")
print()
print("\033[0m[\033[93;1m&\033[0m] LISENSI")
print("\033[0m[\033[94;1m#\033[0m] Informasi")
print("\033[0m[\033[92;1m*\033[0m] Perbarui")
print("\033[0m[\033[91;1m-\033[0m] Keluar")
print()
option = input("\033[0m(\033[105;77;1m/\033[0m) \033[1;77mMasukan opsi: \033[0m")
if option.strip() in '1 kirim'.split():
    write("\n\033[0m[\033[32m●\033[0m] \033[77;1mSedang memproses ...\033[0m")
    sleep(1)
    anonim()
elif option.strip() in '2 motto'.split():
    write("\n\033[0m[\033[32m●\033[0m] \033[77;1mSedang memproses ...\033[0m")
    sleep(1)
    motto()
elif option.strip() in '& 3 lisensi'.split():
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
    input('[ Tekan Enter ]')
    restart()
elif option.strip() in '* 5 perbarui'.split():
    print()
    os.system('git pull origin master')
    print()
    input('\033[0m[ \033[32mTekan Enter \033[0m]')
    restart()
elif option.strip() in '- 0 keluar'.split():
    print("\n\033[0m[\033[1;91m!\033[0m] \033[1;77mKeluar dari program!")
    print()
    sys.exit(1)
else:
    print("\n\033[0m[=\033[1;41;77m Pilihan Salah \033[0m=]")
    print()
    sleep(1)
    restart()
