string = open('text.txt','r',encoding="utf-8").read() # считывание текста из файла

string = string.split() # разделение строки на список слов

print("Количество слов:",len(string))
