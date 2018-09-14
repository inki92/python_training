print("Создание файла и открытие его на запись")
text_file = open("write_it.txt", "w", encoding='utf-8')
text1 = "Строка 1\n"
text2 = "Строка 2\n"
text3 = "Строка 3\n"
text_file.write(text1)
text_file.write(text2)
text_file.write(text3)
text_file.close()
print("Теперь читаю этот файл")
text_file = open("write_it.txt", "r", encoding='utf-8')
print(text_file.read())
print("А теперь метод writelines")
text_file = open("write_it.txt", "w", encoding='utf-8')
lines = [text1, text2, text3]
text_file.writelines(lines)
text_file.close()
print("Печатаю этот файл")
text_file = open("write_it.txt", "r", encoding='utf-8')
#print(text_file.read())
lines = text_file.readlines()
print(lines)
text_file.close()
