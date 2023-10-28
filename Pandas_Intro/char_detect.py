import chardet

with open("aluguel.csv", "rb") as file:
    print(chardet.detect(file.read()))
