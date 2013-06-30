# Greg Smyth
# MOOC Wk 2 Homeword Optional 2
# 30th June 2013
# cipher.py

phrase=raw_input("Enter sentence to encrypt: ")
shift=input("Enter shift value: ")

encoded_phrase=""

for c in phrase:
    # converts a letter to ascii code
    ascii_code = ord(c)

    #checks if upper case letter
    if ascii_code >= 65 and ascii_code <=91:
        shift_code=65
    #checks if lower case letter
    elif ascii_code >= 97 and ascii_code <=123:
        shift_code=97
    else: shift_code=0

    #checks for non-letter characters and keeps if so
    if shift_code == 0:
        new_letter = c
    else:
        new_code = ascii_code+shift
        new_ascii= (new_code - shift_code) % 26 + shift_code
        new_letter = chr(new_ascii)

    encoded_phrase = encoded_phrase + new_letter

print "The encoded phrase is: " + encoded_phrase

