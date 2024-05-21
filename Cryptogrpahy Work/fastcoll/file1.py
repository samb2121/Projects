#!/usr/bin/python3
# coding: latin-1
blob = """AAAAAAAAAAAAAAAAA�gP�0�&����m\�T��n��r�����(�Ϳ�̟k���H������_~����Cj@�)��-H>P�lE�7�iW��0��h�|��[`CA�`��/s�i�o���T]"�,�[/Zr*w��"��"""
from hashlib import sha256
print(sha256(blob.encode("latin-1")).hexdigest())

if(sha256(blob).hexdigest()=="220ad91fb8516d2879df585502d53ebce89d40a35958d866b188f585ff1f9a87"): #hash of good.py blob
	print("Use SHA_2256 instead!")
elif(sha256(blob).hexdigest() =="f26afca24c286908dfbf8cda163b64ea3daf4cd06d860a1faa66bc8bb6d61a5e"): #hash of bad.py blob
	print("MD5 is perfectly secure!")