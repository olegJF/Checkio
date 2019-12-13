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
    def value_verification(_val):
        _val = _val.strip() if _val else _val
        if not _val or _val == 'null':
            return None
        if _val in ('true', 'false'):
            return True if _val == 'true' else False
        elif '"' in _val:
            _val = _val.replace('\\"', '*').replace('"', '').replace('*', '"')
        return int(_val) if _val.isdigit() else _val

    text_lst = [pair for pair in text.split('\n') if pair]
    yaml_dct = {}
    for pair in text_lst:
        key, val = pair.split(':')
        key = key.strip()
        val = value_verification(val)
        yaml_dct[key] = val
    return yaml_dct


if __name__ == '__main__':
    print("Example:")
    # assert yaml('name: Alex\nage: 12') == {'age': 12, 'name': 'Alex'}
    # assert yaml('name: Alex Fox\n'
    #  'age: 12\n'
    #  '\n'
    #  'class: 12b') == {'age': 12,
    #  'class': '12b',
    #  'name': 'Alex Fox'}
    # assert yaml('name: "Alex \\"Fox\\""\n'
    #  'age: 12\n'
    #  '\n'
    #  'class: 12b') == {'age': 12,
    #  'class': '12b',
    #  'name': 'Alex "Fox"'}
    # assert yaml('name: "Alex Fox"\n'
    #  'age: 12\n'
    #  '\n'
    #  'class: 12b') == {'age': 12,
    #  'class': '12b',
    #  'name': 'Alex Fox'}
    # assert yaml('name: "Bob Dylan"\n'
    #  'children: 6\n'
    #  'alive: false') == {'alive': False,
    #  'children': 6,
    #  'name': 'Bob Dylan'}
    # assert yaml('name: "Bob Dylan"\n'
    #  'children: 6\n'
    #  'coding:') == {'children': 6,
    #  'coding': None,
    #  'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
     'children: 6\n'
     'coding: null') == {'children': 6,
     'coding': None,
     'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
     'children: 6\n'
     'coding: "null" ') == {'children': 6, 'coding': 'null', 'name': 'Bob Dylan'}

    tests = [
        {
            "input": ["""name: Alex
age: 12"""],
            "answer": {
              "name": "Alex",
              "age": 12
            }
        },
        {
            "input": ["""name: Alex Fox
age: 12
class: 12b"""],
            "answer": {
              "age": 12,
              "name": "Alex Fox",
              "class": "12b"
            }
        },
        {
            "input": ["""name: "Alex Fox"
age: 12
class: 12b"""],
            "answer": {
              "age": 12,
              "name": "Alex Fox",
              "class": "12b"
            }
        },
        {
            "input": ["""name: "Alex \\"Fox\\""
age: 12
class: 12b"""],
            "answer": {
              "age": 12,
              "name": "Alex \"Fox\"",
              "class": "12b"
            }
        },
        {
          "input": ["""name: "Bob Dylan"
children: 6
alive: false"""],
          "answer": {
            "name": "Bob Dylan",
            "alive": False,
            "children": 6
          }
        },
        {
          "input": ["""name: "Bob Dylan"
children: 6
coding:"""],
          "answer": {
            "coding": None,
            "name": "Bob Dylan",
            "children": 6
          }
        },
        {
          "input": ["""name: "Bob Dylan"
children: 6
coding: null"""],
          "answer": {
            "coding": None,
            "name": "Bob Dylan",
            "children": 6
          }
        },
        {
          "input": ["""name: "Bob Dylan"
children: 6
coding: "null" """],
          "answer": {
            "coding": "null",
            "name": "Bob Dylan",
            "children": 6
          }
        },
        {
            "input": ["""
name: Alex
age: 12"""],
            "answer": {
              "name": "Alex",
              "age": 12
            },
            "explanation": "Extra space at the beginning"
        },
        {
            "input": ["""12: 12"""],
            "answer": {"12": 12},
            "explanation": 'Key can be int'
        },
        {
            "input": ["""name: Bob Dylan
burn: 24 May 1941
resident: Malibu, California, U.S
children: 6"""],
            "answer": {
              "resident": "Malibu, California, U.S",
              "burn": "24 May 1941",
              "name": "Bob Dylan",
              "children": 6
            }
        }
    ]
    for i, t in enumerate(tests):
        assert yaml(t['input'][0]) == t["answer"], i

    print("Coding complete? Click 'Check' to earn cool rewards!")
