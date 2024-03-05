import math

from AlphabetConfig import *


class VigenerCypher:
    def __init__(self, key, type):
        if type == 'by_repeat':
            self.type_vigener = VigenerCypherRepeatedGamma(key)
        if type == 'by_plaintext':
            self.type_vigener = VigenerCypherPlainTextGamma(key)
        if type == 'by_ciphertext':
            self.type_vigener = VigenerCypherCipherTextGamma(key)

    def encrypt(self, x):
        return self.type_vigener.encrypt(x)

    def decrypt(self, y):
        return self.type_vigener.decrypt(y)

    def info(self):
        self.type_vigener.info()


class VigenerCypherRepeatedGamma:
    def __init__(self, key):
        self.key = key

    def encrypt(self, x):
        y = ''
        gamma = self.key * (len(x) // len(self.key)) + self.key[:len(x) % len(self.key)]
        for i in range(len(x)):
            y += A[(A_ID[x[i]] + A_ID[gamma[i]]) % m]
        return y

    def decrypt(self, y):
        x = ''
        gamma = self.key * (len(y) // len(self.key)) + self.key[:len(y) % len(self.key)]
        for i in range(len(y)):
            x += A[(A_ID[y[i]] - A_ID[gamma[i]]) % m]
        return x

    def info(self):
        print(f"Type of gamma: repeated key\n"
              f"key = {self.key}")


class VigenerCypherPlainTextGamma:
    def __init__(self, key):
        self.key = key

    def encrypt(self, x):
        y = ''
        gamma = self.key + x[:len(x) - 1]
        for i in range(len(x)):
            y += A[(A_ID[x[i]] + A_ID[gamma[i]]) % m]
        return y

    def decrypt(self, y):
        x = ''
        x += A[(A_ID[y[0]] - A_ID[self.key[0]]) % m]
        for i in range(1, len(y)):
            x += A[(A_ID[y[i]] - A_ID[x[-1]]) % m]
        return x

    def info(self):
        print(f"Type of gamma: gamma based on plaintext\n"
              f"key = {self.key}")


class VigenerCypherCipherTextGamma:
    def __init__(self, key):
        self.key = key

    def encrypt(self, x):
        y = ''
        y += A[(A_ID[x[0]] + A_ID[self.key[0]]) % m]
        for i in range(1, len(x)):
            y += A[(A_ID[x[i]] + A_ID[y[-1]]) % m]
        return y

    def decrypt(self, y):
        x = ''
        gamma = self.key + y[:len(y) - 1]
        for i in range(len(y)):
            x += A[(A_ID[y[i]] - A_ID[gamma[i]]) % m]
        return x

    def info(self):
        print(f"Type of gamma: gamma based on ciphertext\n"
              f"key = {self.key}")
