import os
from time import *
from tkinter import * 
import pyfiglet
import webbrowser
import socket
import datetime
from faker import *
g = '\033[1;32m' #green
r = '\033[1;31m' #red
v = '\033[1;35m' #vuli
b = '\033[1;36m' #blue fonce
w = '\033[1;37m' #white
#-----------------------------#
#project : search website 
#tools : tkinter
#security : no virous (security)
#---------------------------------#

                                     #_________________________Page1__________________________________________________
def pg1():
    print("""\033[1;31m
    
░██████╗██╗██╗░░░░░███████╗███╗░░██╗████████╗░░░░░░░██████╗░██╗░░██╗░█████╗░░██████╗████████╗
██╔════╝██║██║░░░░░██╔════╝████╗░██║╚══██╔══╝░░░░░░██╔════╝░██║░░██║██╔══██╗██╔════╝╚══██╔══╝
╚█████╗░██║██║░░░░░█████╗░░██╔██╗██║░░░██║░░░█████╗██║░░██╗░███████║██║░░██║╚█████╗░░░░██║░░░
░╚═══██╗██║██║░░░░░██╔══╝░░██║╚████║░░░██║░░░╚════╝██║░░╚██╗██╔══██║██║░░██║░╚═══██╗░░░██║░░░
██████╔╝██║███████╗███████╗██║░╚███║░░░██║░░░░░░░░░╚██████╔╝██║░░██║╚█████╔╝██████╔╝░░░██║░░░
╚═════╝░╚═╝╚══════╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░░░░░░░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═════╝░░░░╚═╝░░░

""")
    to1 = print('\033[1;36m1[*]','\033[1;37mScan \033[1;31m[Ports/Vuln] \033[1;37min web')
    to2 = print('\033[1;36m2[*]','\033[1;37mCreat Files \033[1;31m[Password]')
    to3 = print('\033[1;36m3\033[1;36m[*]','\033[1;37mCreat Files \033[1;31m[Email]')
    to4 = print('\033[1;36m4\033[1;36m[*]','\033[1;37mEncryption\033[1;31m[File encryption]')
    inp1 = input('\033[1;32m>> \033[1;37m')
    if inp1 == '1':
        os.system('cls')
        sleep(2)
        terS()
    if inp1 == '2':
        passwd()
        pass
    if inp1 == '3':
        os.system('clear')
        emails()    
    if inp1 == '4':
        encr()

    
                          #_____________________Search website___________________________________________
def terS():
    print("""

█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░██░░░░░░████████████████░░░░░░██████████░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░████████████████░░▄▀░░██████████░░▄▀░░█
█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░████████████████░░▄▀░░██████████░░▄▀░░█
█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░████░░▄▀░░███░░▄▀░░█████████░░▄▀░░██░░▄▀░░████████████████░░▄▀░░██████████░░▄▀░░█
█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░█████████░░▄▀░░░░░░▄▀░░█░░░░░░░░░░░░░░█░░▄▀░░██░░░░░░██░░▄▀░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█
█░░░░░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░░░███░░▄▀░░█████████░░▄▀░░░░░░▄▀░░█░░░░░░░░░░░░░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█
█████████░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█████░░▄▀░░█████████░░▄▀░░██░░▄▀░░████████████████░░▄▀░░░░░░▄▀░░░░░░▄▀░░█
█░░░░░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░████████████████░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░████████████████░░▄▀░░░░░░▄▀░░░░░░▄▀░░█
█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░██░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░████████████████░░░░░░██░░░░░░██░░░░░░█
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████

""")
    print('\033[1;31m=8='*121)
    info = print('\033[1;32mif you want search web site write name web example : \033[1;35mEnter name-W : google')
    inp = input('\033[1;37mEnter The name-w : ')
    op = webbrowser.open('https://www.'+inp+'.com')
    op2 = webbrowser.open('https://www.'+inp+'.org')
    op3 = webbrowser.open('https://www.'+inp+'.net')
    op4 = webbrowser.open('http://www.'+inp+'.com')
    op5 = webbrowser.open('http://www.'+inp+'.net')
    op4 = webbrowser.open('http://www.'+inp+'.org')
    inf = print('\033[1;31mWarning:\n \033[1;33mIf a website opens, write to me the name of the site along with its format: .com, .net, or .org. When you write the name along with its format, the site will be scanned from the open ports and some vulnerabilities will be guessed.')
     
    url = input('\033[1;33mEnter the name website and domine [example.com/example.net/example.org]: ')
    ports = [21,22,25,53,51,455,3306,995,111,143,443]
    if 'http' not in url:
        os.system('clear')
        ip = socket.gethostbyname(url)
        for port in ports:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            scan = s.connect_ex((ip,port))
            if scan == 0:
                name = socket.getservbyport(port)
                print(f'\033[1;35mIP > \033[1;36m{ip}:({port}\{name}) \033[1;32m>> is [Open]')
            else:
                print(f'\033[1;35mIP > \033[1;36m{ip}:({port}\{name}) \033[1;31m>> is [Close]')

    
                
                inf2 = print('\033[1;31mWarning :\n \033[1;33mTo know that the site is infected with vulnerabilities, type in the Linux system [nmap --script=* -p[port] [ip] ]')
                for i in range(4):
                    vulns = print('\033[1,31mFamous vulnerabilities :')
                    sleep(1)
                    ftp = print('\033[1;35m21/ftp >> Vmsftp , Pure-FTPd ')
                    sleep(1)
                    smb = print('\033[1;35m445/smb >> ms10-017 [smb]')
                    sleep(1)
                    ssh = print('\033[1;35m22/ssh >> ssh[ssh]')
                    break
                my_web = input('open my web (Y/N) :')
                if my_web == 'Y'or'y':
                    webbrowser.open('https://tatashopeseif9ufs9ufde.on.drv.tw/z/page1.html')
                if my_web == 'N'or'n':
                    exit

        os.system("clear")
                    
                             #__________________________________Creat Emails____________________________________________________
def emails():
    fk = Faker()
    print('\033[1;33m<<',' \033[1;31mCreat Emails please wait ''\033[1;33m>>')
    sleep(3)
    for i in range(20):
        sleep(0.005)
        print('\033[1;32m{Faker Emails please Wait}')
    os.system('cls')
    print('\033[1;31m='*121)
    sleep(2)
    print("""\033[1;37m

───────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─██████──────────██████─██████████████─██████████─██████─────────██████████████─
─██░░░░░░░░░░██─██░░██████████████░░██─██░░░░░░░░░░██─██░░░░░░██─██░░██─────────██░░░░░░░░░░██─
─██░░██████████─██░░░░░░░░░░░░░░░░░░██─██░░██████░░██─████░░████─██░░██─────────██░░██████████─
─██░░██─────────██░░██████░░██████░░██─██░░██──██░░██───██░░██───██░░██─────────██░░██─────────
─██░░██████████─██░░██──██░░██──██░░██─██░░██████░░██───██░░██───██░░██─────────██░░██████████─
─██░░░░░░░░░░██─██░░██──██░░██──██░░██─██░░░░░░░░░░██───██░░██───██░░██─────────██░░░░░░░░░░██─
─██░░██████████─██░░██──██████──██░░██─██░░██████░░██───██░░██───██░░██─────────██████████░░██─
─██░░██─────────██░░██──────────██░░██─██░░██──██░░██───██░░██───██░░██─────────────────██░░██─
─██░░██████████─██░░██──────────██░░██─██░░██──██░░██─████░░████─██░░██████████─██████████░░██─
─██░░░░░░░░░░██─██░░██──────────██░░██─██░░██──██░░██─██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██████████████─██████──────────██████─██████──██████─██████████─██████████████─██████████████─
───────────────────────────────────────────────────────────────────────────────────────────────
""")
    while 1:
        sleep(0.5)
        em = print(fk.safe_email())
        pass

def passwd():
    fk = Faker()
    print('\033[1;33m<<',' \033[1;31mCreat Emails please wait ''\033[1;33m>>')
    sleep(3)
    for i in range(20):
        sleep(0.005)
        print('\033[1;32m{Faker Emails please Wait}')
        os.system('clear')
    print('\033[1;31m='*121)
    sleep(2)
    print("""\033[1;37m
          
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─██████████████─██████████████─██████████████─██████──────────██████─██████████████─████████████████───████████████───
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──────────██░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░████─
─██░░██████░░██─██░░██████░░██─██░░██████████─██░░██████████─██░░██──────────██░░██─██░░██████░░██─██░░████████░░██───██░░████░░░░██─
─██░░██──██░░██─██░░██──██░░██─██░░██─────────██░░██─────────██░░██──────────██░░██─██░░██──██░░██─██░░██────██░░██───██░░██──██░░██─
─██░░██████░░██─██░░██████░░██─██░░██████████─██░░██████████─██░░██──██████──██░░██─██░░██──██░░██─██░░████████░░██───██░░██──██░░██─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░██──██░░██─██░░██──██░░██─██░░░░░░░░░░░░██───██░░██──██░░██─
─██░░██████████─██░░██████░░██─██████████░░██─██████████░░██─██░░██──██░░██──██░░██─██░░██──██░░██─██░░██████░░████───██░░██──██░░██─
─██░░██─────────██░░██──██░░██─────────██░░██─────────██░░██─██░░██████░░██████░░██─██░░██──██░░██─██░░██──██░░██─────██░░██──██░░██─
─██░░██─────────██░░██──██░░██─██████████░░██─██████████░░██─██░░░░░░░░░░░░░░░░░░██─██░░██████░░██─██░░██──██░░██████─██░░████░░░░██─
─██░░██─────────██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██████░░██████░░██─██░░░░░░░░░░██─██░░██──██░░░░░░██─██░░░░░░░░████─
─██████─────────██████──██████─██████████████─██████████████─██████──██████──██████─██████████████─██████──██████████─████████████───
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
""")
    while 1:
        sleep(0.5)
        pas = print('\033[1;37m'+fk.name())
        pass


def encr():
    os.system('git clone https://github.com/dyne/Tomb')
    print("""\033[1;33m


██████████████████████████████████
█▄─▄▄─█▄─▀█▄─▄█─▄▄▄─█▀▀▀▀▀██▄─▄▄▀█
██─▄█▀██─█▄▀─██─███▀█████████─▄─▄█
▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▀▀▀▀▀▀▀▄▄▀▄▄▀
""")
    inf = print('\033[1;31mWarning :\n \033[1;36mWrite name file example : test.txt for encryption or folder test')
    dec = print('\033[1;31m1\033[1;36m[*]','\033[1;37mEncryption\033[1;34m[File encryption]')
    dec = print('\033[1;31m2\033[1;36m[*]','\033[1;37mDecryption\033[1;34m[File encryption key]')
    inp1 = input('\033[1;32m>>')
    if inp1 == '1':
        na= input("Enter the file name >")
        print(na)
        en = os.system('tomb dig -s {na}.tomb')
        print(en)
        pass
    if inp1 == '2':
        for i in range(150):
            sleep(0.006)
            print('\033[1;35mPlease Enter the Password for encryption file')
        os.system('clear')
        os.system('tomb forge {en}.key -f')
    
    pass
    
pg1()



