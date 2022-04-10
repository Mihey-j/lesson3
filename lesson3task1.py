number = {'zero': 'ноль',
              'one': 'один',
              'two': 'два',
              'three': 'три',
              'four': 'четыре',
              'five': 'пять',
              'six': 'шесть',
              'seven': 'семь',
              'eight': 'восемь',
              'nine': 'девять',
              'ten': 'десять'}
def num_translate(english):
    return number.get(english)
print(num_translate(input('Введите числовое значение, по английски, от 0 до 10: ')))
