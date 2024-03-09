from AlphabetConfig import *


class VigenereCypher:
    def __init__(self, key, type):
        if type == 'by_repeat':
            self.type_vigener = VigenereCypherRepeatedGamma(key)
        if type == 'by_plaintext':
            self.type_vigener = VigenereCypherPlainTextGamma(key)
        if type == 'by_ciphertext':
            self.type_vigener = VigenereCypherCipherTextGamma(key)

    def encrypt(self, x):
        return self.type_vigener.encrypt(x)

    def decrypt(self, y):
        return self.type_vigener.decrypt(y)

    def info(self):
        self.type_vigener.info()


class VigenereCypherRepeatedGamma:
    def __init__(self, key):
        self.__key = key

    def encrypt(self, x):
        y = ''
        index_of_letter_in_key = 0
        for i in x:
            if i not in ALPHABET:
                y += i
            else:
                y += A[(A_ID[i] + A_ID[self.__key[index_of_letter_in_key]]) % m]
                index_of_letter_in_key = (index_of_letter_in_key + 1) % len(self.__key)
        return y

    def decrypt(self, y):
        x = ''
        index_of_letter_in_key = 0
        for i in y:
            if i in ALPHABET:
                x += A[(A_ID[i] - A_ID[self.__key[index_of_letter_in_key]]) % m]
                index_of_letter_in_key = (index_of_letter_in_key + 1) % len(self.__key)
            else:
                x += i
        return x

    def info(self):
        print(f"Type of gamma: repeated key\n"
              f"key = {self.__key}")


class VigenereCypherPlainTextGamma:
    def __init__(self, key):
        self.__key = key

    def encrypt(self, x):
        y = ''
        last_char_in_gamma = self.__key
        for i in x:
            if i not in ALPHABET:
                y += i
            else:
                y += A[(A_ID[i] + A_ID[last_char_in_gamma]) % m]
                last_char_in_gamma = i
        return y

    def decrypt(self, y):
        x = ''
        last_char_in_gamma = self.__key
        for i in y:
            if i not in ALPHABET:
                x += i
            else:
                x += A[(A_ID[i] - A_ID[last_char_in_gamma]) % m]
                last_char_in_gamma = x[-1]
        return x

    def info(self):
        print(f"Type of gamma: gamma based on plaintext\n"
              f"key = {self.__key}")


class VigenereCypherCipherTextGamma:
    def __init__(self, key):
        self.__key = key

    def encrypt(self, x):
        y = ''
        last_char_in_gamma = self.__key
        for i in x:
            if i not in ALPHABET:
                y += i
            else:
                y += A[(A_ID[i] + A_ID[last_char_in_gamma]) % m]
                last_char_in_gamma = y[-1]
        return y

    def decrypt(self, y):
        x = ''
        last_char_in_gamma = self.__key
        for i in y:
            if i not in ALPHABET:
                x += i
            else:
                x += A[(A_ID[i] - A_ID[last_char_in_gamma]) % m]
                last_char_in_gamma = i
        return x

    def info(self):
        print(f"Type of gamma: gamma based on ciphertext\n"
              f"key = {self.__key}")
