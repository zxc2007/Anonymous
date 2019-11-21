#!/usr/bin/python
# Anonymous
# Recode by Senja
# Github: github.com/thedarksec/Anonymous

import os, sys, time, random, requests

os.system('clear')
time.sleep(1)

print("\033[0m")
print("\033[0mAnonymous\033[0m Email by anonymouse.org")
print("The 4chan.org \033[1;4mHacktivist\033[0m Global Groups \n")
to = raw_input('\033[0m[\033[1;91m-\033[0m] \033[1;77mTo: \033[0m')
subject = raw_input('\033[0m[\033[1;96m#\033[0m] \033[1;77mSubject: \033[0m')
message = raw_input('\033[0m[\033[1;94m*\033[0m] \033[1;77mmessage: \033[0m')

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
    print("\033[0m[\033[1;93m+\033[0m] \033[1;77mEmail Sent!")
    print("\033[0m[\033[1;92m!\033[0m] \033[1;77mIn order to increase your privacy, the anonymous e-mail will be randomly delayed up to 12 hours")
