#!/usr/bin/python3

import sys
from collections import Counter

#taken from Wikipedia
letter_freqs = {
    'A': 0.08167,
    'B': 0.01492,
    'C': 0.02782,
    'D': 0.04253,
    'E': 0.12702,
    'F': 0.02228,
    'G': 0.02015,
    'H': 0.06094,
    'I': 0.06966,
    'J': 0.00153,
    'K': 0.00772,
    'L': 0.04025,
    'M': 0.02406,
    'N': 0.06749,
    'O': 0.07507,
    'P': 0.01929,
    'Q': 0.00095,
    'R': 0.05987,
    'S': 0.06327,
    'T': 0.09056,
    'U': 0.02758,
    'V': 0.00978,
    'W': 0.02361,
    'X': 0.00150,
    'Y': 0.01974,
    'Z': 0.00074
}

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def pop_var(s):
    """Calculate the population variance of letter frequencies in given string."""
    freqs = Counter(s)
    mean = sum(float(v)/len(s) for v in freqs.values())/len(freqs)  
    return sum((float(freqs[c])/len(s)-mean)**2 for c in freqs)/len(freqs)

def key_length(cipher):
    length = len(cipher)
    count = [0]*(length - 1)
    keylen = [0]*(length - 1)
    max_count = 0
    current_count = 0
    num = 0
    n = 100
    for i in range(length):
        temp_cipher = cipher[0:length - (i + 1)]
        for j in range(len(temp_cipher)):
            if (temp_cipher[j] == cipher[j+(i+1)]):
                count[i] += 1
    j = 0
    for i in range(length - 1):
        if(count[i] < n):
            j += 1
        else:
            j += 1
            keylen[i] = j
            j = 0
    j = 0
    for i in range(length - 1):
        current_count = 0
        for j in range(length - 1):
            if(keylen[i] != 0):
                if (keylen[i] == keylen[j]):
                    current_count += 1
                if (current_count > max_count):
                    max_count = current_count
                    num = keylen[i]
    return num

def find_key(cipher, keylength):
    key = [0]*keylength
    length  = len(cipher)

    for i in range(keylength):
        count = Counter()
        alph_cipher = [0]*26
        alph = [0]*26
        s = 0.0
        sumi = [0]*26
        if (i < length%7):
            templen = int((length - (length%7))/7) + 1
        else:
            templen = int((length - (length%7))/7)
        temp_cipher = [0]*(templen)    
        j = i
        x = 0
        while ( j < length):
            temp_cipher[x] = cipher[j]
            j += 7
            x += 1
        count.update(temp_cipher)
        j = 0
        for char in alphabet:
            alph_cipher[j] = (count[char])/templen
            alph[j] = letter_freqs[char]
            j += 1
        for j in range(26):
            s = 0.0
            for k in range(26):
                t = (k+j)%26
                s += (alph[k]*alph_cipher[t])
            sumi[j] = s
        Num = sumi.index(max(sumi)) 
        key[i] = chr(Num+97)
    return key

def vigenere_decrypt(cipher, key):
    decrypted_text = []
    key_length = len(key)
    
    for i, char in enumerate(cipher):
        if char.isalpha():
            char_offset = ord(char) - ord(key[i % key_length])
            decrypted_char = chr(((char_offset % 26) + 26) % 26 + ord('A'))
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)
    
    return ''.join(decrypted_text)

if __name__ == "__main__":
    # Read ciphertext from stdin
    # Ignore line breaks and spaces, convert to all upper case
    cipher = sys.stdin.read().replace("\n", "").replace(" ", "").upper()

    # Determine the key length and find the key
    keylength = key_length(cipher)
    key = find_key(cipher, keylength)
    real_key = ",".join(key)
    print(real_key.replace(",", "").upper())
