from VigenerCypher import VigenerCypher

cypher = None
print("Введите ключ и тип (by_repeat/by_plaintext/by_ciphertext) для шифра виженера через пробел соответственно.")
values = input().split()
cypher = VigenerCypher(values[0], values[1])
while True:
    mode = input("Введите операцию (E/D/EText/DText/Info - Encrypt line/Decrypt line/Encrypt text/Decrypt text/Get information about key(s) in the cypher/)\n")
    if mode == "Info":
        cypher.info()
        continue
    print("Введите текст/слово для зашифрования/расшифрования\n"
          "(Заглавные буквы автоматически заменятся на строчные)")
    if mode == "EText":
        print("(Введите пустую строку для того, чтобы закончить ввод)")
        text = []
        line = input().lower()
        while line != '':
            text.append(line)
            line = input().lower()
        out = [cypher.encrypt(i) for i in text]
        for i in out:
            print(i)
    elif mode == "DText":
        print("(Введите пустую строку для того, чтобы закончить ввод)")
        text = []
        line = input().lower()
        while line != '':
            text.append(line)
            line = input().lower()
        out = [cypher.decrypt(i) for i in text]
        for i in out:
            print(i)
    elif mode == "E":
        print(cypher.encrypt(input().lower()))
    elif mode == "D":
        print(cypher.decrypt(input().lower()))

