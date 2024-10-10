string = open('text.txt','r',encoding="utf-8").read()

slova = 0

if string == "":
    print("Количество слов: 0")
    quit()

for i in string:
    if i == " ":
        slova +=1

print("Количество слов:",slova+1)
