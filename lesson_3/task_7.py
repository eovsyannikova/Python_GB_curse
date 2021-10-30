def fun_cap(text):
    text = text.capitalize()
    return text


my_text = input('Введите текст: ')
rez_text = ""

for word in my_text.split():
    rez_text += "{} ".format(fun_cap(word))


print(rez_text)
