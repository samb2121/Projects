#!/usr/bin/python3
# coding: latin-1
blob = """AAAAAAAAAAAAAAAAAøgP€0Â&¦Ùøm\”T¯8nÀár€žº°Ã(‹Í¿ìÌŸk·ëùHùÔŸ»¦¾Å_~´©Cj@˜)­á-H>PlEâ7ñiW„à°ãíh|é¿Û[`CAå`­Ž/sÿi·o‘ñGT]"ò,•[/Zr*wZÒ"‚"""
from hashlib import sha256

good = "4c6216031faac3a8044d78d1ec73ca0bda2e64ff25804b219973ef335f186daa"
print(sha256(blob.encode("latin-1")).hexdigest())

if sha256(blob.encode("latin-1")).hexdigest() == good: 
	print("Use SHA-256 instead!")
else:
	print("MD5 is perfectly secure!")