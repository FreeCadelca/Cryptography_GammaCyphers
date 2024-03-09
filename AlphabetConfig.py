# import pprint

ALPHABET = (
        [chr(i) for i in list(range(ord('a'), ord('z') + 1))] +
        [str(i) for i in range(10)] +
        [' ', ',', '-', '\'', ':', '.', ';', '!', '“', "”", "\"", '?', '%']
)
# эта часть алфавита для части лабораторной с криптоанализом,
# потому что в ней нужно шифровать большие тексты, алфавит которых
# состоит из более, чем 27 символов.
A = {i: ALPHABET[i] for i in range(len(ALPHABET))}
A_ID = {A[i]: i for i in A.keys()}
m = len(ALPHABET)

# pprint.pprint(A)
# for i in input():
#     print(A_ID[i])
