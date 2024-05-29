# 4
# HelloGood Morning
# abcd123Fghy
# India
# Progoto.c

n = int(input())
l = []
for i in range(n):
    x = str(input())
    l.append(x)


def isValid():
    validCount = 0
    invalidCount = 0

    print(l)
    for word in l:
        if " " in word:
            word = word.replace(" ", "")
        print(word.isalpha())



isValid()


