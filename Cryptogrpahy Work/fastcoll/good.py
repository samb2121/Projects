#!/usr/bin/python3
# coding: latin-1
blob = """AAAAAAAAAAAAAAAAA�gP�0�&����m\�T��n��r�����(�Ϳ�̟k���H������_~����Cj@�)��-H>P�lE�7�iW��0��h�|��[`CA�`��/s�i�o���T]"�,�[/Zr*w��"��"""
from hashlib import sha256

good = "4c6216031faac3a8044d78d1ec73ca0bda2e64ff25804b219973ef335f186daa"
evil = "8edd5855971b7766e5612037f1da8721f4e1e4fbfd8461ac072d8cc933cf39c3"


if good == sha256(blob.encode("latin-1")).hexdigest(): 
	print("Use SHA-256 instead!")
#if evil == sha256(blob.encode("latin-1")).hexdigest(): 
else:
	print("MD5 is perfectly secure!")