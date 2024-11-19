#Задача "Записать и запомнить":

#Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name - название файла для записи, strings - список строк для записи.
                                          #Функция должна:
#Записывать в файл file_name все строки из списка strings, каждая на новой строке.
#Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
#а значением - записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.
#Пример полученного словаря:
#{(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}
                #Где:
#1, 2 - номера записанных строк.
#0, 16 - номера байт, на которых началась запись строк.
#'Text for tell.', 'Используйте кодировку utf-8.' - сами строки.

def custom_write(file_name, strings):
    string_positions = {} # Создаем пустой словарь для хранения позиций строк

    with open(file_name, 'w', encoding='utf-8') as file:  # Открываем файл с именем file_name для записи (режим 'w') с кодировкой 'utf-8'
                  # Проходим по списку строк с их индексами, начиная с 1
        for i, string in enumerate(strings, start=1):
                  # Получаем текущую позицию в байтах перед записью строки
            position = file.tell()
                  # Записываем строку в файл, добавляя символ новой строки ('\n')
            file.write(string + '\n')
            # Сохраняем информацию о позиции и строке в словарь
            string_positions[(i, position)] = strings
    return string_positions
    file.close()

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)