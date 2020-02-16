#!/usr/bin/python
# -*- coding: utf-8 -*-
# Anonymous
# Coded by Nedi Senja
# Github: https://github.com/stepbystepexe/Anonymous

from __opt__ import *
import os, sys, time, random, requests, marshal

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

example = """\033[0;44;1;77m[      Anonymous e-Mail, My Github: @stepbystepexe       ]\033[0m"""

def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()

def loads():
    x = [
     '.   ', '..  ', '... ']
    for o in x:
        print '\r\033[0m[\033[94;1m\xe2\x97\x8f\033[0m] \033[0mSedang mengirim ' + o,
        sys.stdout.flush()
        time.sleep(1)

def anonim():
    print
    to = raw_input('\n\033[0m[ \033[91mKepada \033[0m] \033[4m')
    subject = raw_input('\033[0m[ \033[92mSubjek \033[0m] \033[4m')
    message = raw_input('\033[0m[ \033[94mPessan \033[0m] \033[4m')
    print
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
        print("\033[0m[\033[1;96m+\033[0m] \033[1;77mEmail terkirim sukses !")
        print("\033[0m[\033[1;95m!\033[0m] \033[1;77mIn order to increase your privacy, the anonymous e-mail will be randomly delayed up to 12 hours")
        print

os.system('clear')
os.system('reset')
time.sleep(1)
print
print(logo)
print(example)
print
print("\033[0m[\033[1;96mあ\033[0m] \033[1;77mKirim Email Anonim")
print
print("\033[0m[\033[93;1m&\033[0m] LISENSI")
print("\033[0m[\033[94;1m#\033[0m] Informasi")
print("\033[0m[\033[92;1m*\033[0m] Perbarui")
print("\033[0m[\033[91;1m-\033[0m] Keluar")
print
option = raw_input("\033[0m[\033[1;95m/\033[0m] \033[1;77mMasukan opsi: \033[0m")
if option.strip() in 'あ 1 kirim'.split():
    anonim()
elif option.strip() in '& 2 lisensi'.split():
    print
    os.system('nano LICENSE')
    print
    restart()
elif option.strip() in '# 3 info'.split():
    os.system('clear')
    print(example)
    os.system('toilet -f smslant Anonim')
    print(info)
    time.sleep(1)
    print
    raw_input('[ Tekan Enter ]')
    restart()
elif option.strip() in '* 4 perbarui'.split():
    print
    os.system('git pull origin master')
    print
    raw_input('\033[0m[ \033[92mTekan Enter \033[0m]')
    restart()
elif option.strip() in '- keluar 0'.split():
    print("\n\033[0m[\033[1;91m!\033[0m] \033[1;77mKeluar dari program!")
    print
    sys.exit(1)
else:
    print("\n\033[0m[=\033[1;41;77m Pilihan Salah \033[0m=]")
    print
    time.sleep(1)
    restart()
