
def file_edit(text,name):
    file = open(name, 'a+')
    if file.tell() == 0:
        file.write(f'{text}')
    else:
        file.write(f'\n{text}')
    file.close()

text = input("Введите текст: ")
name = input("Введите имя файла: ")

file_edit(text,name)

def even(name):
    with open(name, 'r') as file:
        readlines = file.readlines()
        for i in range(1,len(readlines),2):
            print(readlines[i])

print("Вывод чётных строк:" )
even(name)
