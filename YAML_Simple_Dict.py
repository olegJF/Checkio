'''
Первый шаг - это преобразование ключ-значение. Ключом может быть любая
строка, из латинских букв и цифр. Значением может быть однострочная строка
(которая состоит из пробелов, латинских букв и цифр) или число (int).
Покажу несколько примеров:
name: Alex
age: 12
Преобразуется в объект.
{
  "name": "Alex",
  "age": 12
}

Обратите внимание, что число автоматически получило тип int.
Еще один пример показывает, что строка может содержать пробелы:
name: Alex Fox
age: 12
class: 12b

Будет преобразован в следующий объект.
{
  "age": 12,
  "name": "Alex Fox",
  "class": "12b"
}

Обратите внимание на несколько вещей. Между строкой "age" и строкой
"class" есть пустая строка, которая не мешает парсингу. Класс начинается
с цифр, но имеет буквы, а значит не может быть преобразован в цифры,
поэтому его тип остался строкой (str).
'''


def yaml(text):
    text_lst = [pair for pair in text.split('\n') if pair]
    yaml_dct = {}
    for pair in text_lst:
        key, val = pair.split(':')
        key = key.strip()
        val = val.strip()
        yaml_dct[key] = int(val) if val.isdigit() else val
    return yaml_dct


if __name__ == '__main__':
    print("Example:")
    print(yaml("""name: Alex
age: 12"""))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml("""name: Alex
age: 12""") == {'age': 12, 'name': 'Alex'}
    assert yaml("""name: Alex Fox
    age: 12

class: 12b""") == {'age': 12,
 'class': '12b',
 'name': 'Alex Fox'}
    print("Coding complete? Click 'Check' to earn cool rewards!")
