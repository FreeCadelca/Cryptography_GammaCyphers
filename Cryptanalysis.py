from VigenereCypher import *
from frequency_of_symbols_in_data import *


def DecryptingOfCesarCypher(ciphertext):
    frequency_ciphertext = {A[i]: 0 for i in A}
    n = 0
    for i in ciphertext:
        if i in ALPHABET:
            frequency_ciphertext[i] += 1
            n += 1
    for i in frequency_ciphertext.keys():
        frequency_ciphertext[i] /= n
    frequency_ciphertext_sorted = sorted([(i, frequency_ciphertext[i]) for i in frequency_ciphertext.keys()],
                                         key=lambda x: -x[1])
    frequency_of_data_sorted = sorted([(i, frequency_of_data[i]) for i in frequency_of_data.keys()],
                                      key=lambda x: -x[1])
    return (A_ID[frequency_ciphertext_sorted[0][0]] - A_ID[frequency_of_data_sorted[0][0]]) % m


def hack_Vigenere_with_key_given_length(text, length):
    parts_of_text = [''] * length
    current_number_of_symbol = 0
    for i in text:
        if i in ALPHABET:
            parts_of_text[current_number_of_symbol] += i
            current_number_of_symbol = (current_number_of_symbol + 1) % length
    key = ''
    for part in parts_of_text:
        key += A[DecryptingOfCesarCypher(part)]
    return key


def check_decrypted_text(decrypted_text):
    if ('the' in decrypted_text) and ('if' in decrypted_text) and ('but' in decrypted_text):
        return True


print('Enter the text:')
text = ''
line = input().lower()
while line != '':
    text += line + '\n'
    line = input().lower()
mode = input('Введите тип шифра Виженера '
             '(1 - повторение/2 - самоключ по открытому тексту/3 - самоключ по шифртексту)\n')
if mode == '1':
    for length_of_key in range(2, 15):
        potential_key = hack_Vigenere_with_key_given_length(text, length_of_key)
        cypher = VigenereCypher(potential_key, 'by_repeat')
        decrypted_text = cypher.decrypt(text)
        if check_decrypted_text(decrypted_text):
            print(potential_key)
else:
    for potential_key in ALPHABET:
        cypher = VigenereCypher(potential_key, 'by_plaintext' if mode == '2' else 'by_ciphertext')
        decrypted_text = cypher.decrypt(text)
        if check_decrypted_text(decrypted_text):
            print(potential_key)
