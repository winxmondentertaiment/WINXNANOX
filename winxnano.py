# script by Winxmond Entertaiment
# support us

#import
import os
import time
import random
from colorama import Fore, Back, Style
import sys
import requests

#variable warna
me = Fore.RED
hi = Fore.GREEN
ku = Fore.YELLOW
bi = Fore.BLUE
ma = Fore.MAGENTA
cy = Fore.CYAN
pu = Fore.WHITE

#variable gaya
tt = Style.BRIGHT
no = Style.NORMAL
te = Style.DIM

#variable back
mer = Back.RED
hij = Back.GREEN
bir = Back.BLUE
kun = Back.YELLOW
mag = Back.MAGENTA
cya = Back.CYAN
put = Back.WHITE
hit = Back.BLACK

#script UTAMA
os.system("clear")
print("Mohon menunggu...")
time.sleep(2)
os.system("clear")
print(me + """╔╦═╦╗╔══╗╔═╦╗╔╗╔╗╔═╦╗╔══╗╔═╦╗╔═╗
║║║║║╚║║╝║║║║╚╗╔╝║║║║║╔╗║║║║║║║║
║║║║║╔║║╗║║║║╔╝╚╗║║║║║╠╣║║║║║║║║
╚═╩═╝╚══╝╚╩═╝╚╝╚╝╚╩═╝╚╝╚╝╚╩═╝╚═╝""")
print(Style.RESET_ALL)
print(cya + "V2.0")
print(Style.RESET_ALL)
print(mag + "By WinxScript")
print(Style.RESET_ALL)
print()
print(ku + "1. Owner ( Winxmond Entertaiment Co. )")
print()
print(ma + "2. Blog Kami")
print()
print(hi + "3. instalasi tools Sqlmap")
print()
print(bi + "4. pembuat biodata otomatis")
print(Style.RESET_ALL)
print()
print()
__main__ = input(tt + "Enter Your Inputs/Choice : ")

if __main__ == "1":
 os.system("clear")
 time.sleep(0.5)
 print("press any" +  kun + " key to continue...")
 input()
 print(Style.RESET_ALL)
 os.system("xdg-open https://t.me/WinxmondEnt")

 print("jangan apa apain akun gua ya anak baik :)")
 print()

elif __main__ == "2":
 os.system("clear")
 time.sleep(0.5)
 print("press any" +  kun + " key to continue...")
 input()
 print(Style.RESET_ALL)
 os.system("xdg-open https://wecpow.blogspot.com/?m=1")
else:
  print("apakah anda salah mengetik??, atau mungkin anda tidak mengetik??")
  print()

if __main__ == "3":
 os.system("clear")
 time.sleep(0.5)
 print(kun + "instalasi sedang berjalan")
 print(Style.RESET_ALL)
 time.sleep(1)
 os.system("git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev")
 os.system("mv sqlmap-dev /sdcard")
 time.sleep(0.4)
 print(me + "[!] INFO")
 print(Style.RESET_ALL)
 print("instalasi telah berhasil!!, file sqlmap kini ada di sdcard.")
 print()

elif __main__ == "4":
 os.system("clear") 
 nama = input("nama lengkap/nama samaran : ")
 umur = input("umur/umur palsu anda : ")
 bakat = input("bakat anda : ")
 jenisk = input("jenis kelamin : ")
 os.system("clear")
 print(kun + "sedang membuat biodata...")
 print(Style.RESET_ALL)
 time.sleep(1)
 print(f"nama lengkap/nama samaran : {nama}")
 print(f"umur/umur palsu anda : {umur}")
 print(f"bakat anda : {bakat}")
 print(f"jenis kelamin : {jenisk}")
 