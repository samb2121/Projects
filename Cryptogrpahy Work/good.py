#!/usr/bin/python3
# coding: latin-1
blob = """AAAAAAAAAAAAAAAAA�gP�0�&����m\�T��n��r�����(�Ϳ�̟k���H������_~����Cj@�)��-H>P�lE�7�iW��0��h�|��[`CA�`��/s�i�o���T]"�,�[/Zr*w��"��"""
from hashlib import sha256

good = "4c6216031faac3a8044d78d1ec73ca0bda2e64ff25804b219973ef335f186daa"
print(sha256(blob.encode("latin-1")).hexdigest())

if sha256(blob.encode("latin-1")).hexdigest() == good: 
	print("Use SHA-256 instead!")
else:
	print("MD5 is perfectly secure!")