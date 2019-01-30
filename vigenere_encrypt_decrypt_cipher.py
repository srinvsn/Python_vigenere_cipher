""" Encrypts and decrypts a message using using an alpha, numeric or alphanumeric key """


""" Encrypts a string message (m) using an alpha, numeric or alphanumeric key (k) """


def vigenere_encrypt(m, k):
    list_m = list(m)
    list_k = list(k)
    encrypt = ''
    for (char_m, char_k) in zip(list_m, list_k):
        if ((ord(char_k) - ord('a')) + (ord(char_m) - ord('a'))) > (ord('z') - ord('a')):
            encrypt += chr((ord(char_m) + ord(char_k) - ord('z') - 1))
        else: encrypt += chr((ord(char_m) + ord(char_k) - ord('a')))
    return encrypt


""" Decrypts a string message (msg) using an alpha, numeric or alphanumeric key (k) """


def vigenere_decrypt(msg, k):
    list_msg = list(msg)
    list_k = list(k)
    decrypt = ''
    decrypt.lower()
    for (char_msg, char_k) in zip(list_msg, list_k):
        if ord(char_k) < ord('a'):
            decrypt += chr((ord(char_msg) - int(char_k)))
        if ord(char_msg) > ord(char_k) or ord(char_msg) == ord(char_k):
            decrypt += chr(ord(char_msg) - ord(char_k) + ord('a'))
        else: decrypt += chr(ord(char_msg) - ord(char_k) + ord('z') + 1)
    return ''.join([i for i in decrypt if i.isalpha()])


""" Example with message and key from Wikipedia with the exception of the letter 'e' being replaced by '4' """
print vigenere_decrypt("lxfopvefrnhr", "l4monlemonl4")
