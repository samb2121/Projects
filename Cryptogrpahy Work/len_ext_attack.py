#!/usr/bin/python3

import sys
from urllib.parse import quote, urlparse
from pymd5 import md5, padding

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} TARGET_URL", file=sys.stderr)
        sys.exit(-1)

    target_url = sys.argv[1]

    # PARSING:

# Find the position of the '&' character
ampersand_position = target_url.index('&') + 1
# Extract the portion of the URL after the '&'
command_param = target_url[ampersand_position:]

# Find the position of the 'token=' parameter and extract the token value
token_start_position = target_url.index('token=') + len('token=')

# Initialize an empty string for the extracted token
extracted_token = ''

# Iterate through the characters between token_start_position and ampersand_position - 1
for i in range(token_start_position, ampersand_position - 1):
    extracted_token += target_url[i]

# Calculate the total length including command and padding
total_length = len(command_param) + 8

# URL CREATION:

# Calculate the padding for the desired bit length and the bit length
calculated_padding = padding(total_length * 8)
bit_length = (total_length + len(calculated_padding)) * 8

# Create an MD5 hash object with the extracted token and bit length
md5_hash = md5(state=bytes.fromhex(extracted_token), count=bit_length)

# Define the extension string
extension_string = "&command=UnlockSafes"

# Update the MD5 hash with the extension
md5_hash.update(extension_string)

# Retrieve the new token value
new_token = md5_hash.hexdigest()

# Construct the modified URL
modified_url = f'https://project1.ecen4133.org/autograder/lengthextension/api?token={new_token}&{command_param}{quote(calculated_padding)}{extension_string}'

# Print the modified URL
print(modified_url)





