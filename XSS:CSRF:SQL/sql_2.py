import os, random, re, time, hashlib

while(True):
    
    pwd = ""
    for i in range(0,4):
        x = str(random.randint(0, 1000000))
        pwd += x

    md5s =  hashlib.md5(pwd.encode()).digest()


    if ( md5s.find(b"'='") != -1):
        print(md5s)
        print(pwd)
        
        break