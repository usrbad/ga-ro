import random as r
import string
from data.data_types import DataTypes as D

# Функция get_random_string возвращает рандомную строку, составленную из символов в соответствии с:
# string_length - длина строки
# data_type - тип данных из словаря TYPES класса DataTypes
def get_random_string(string_length, data_type: string):
    return ''.join([r.choice(data_type) for j in range(string_length)])

# Функция get_random_list возвращает рандомный список из списков с данными в соответствии с:
# field - поле, список для которого требуется получить
def get_random_list(field):
    if field == 'gender':
        random_length = r.randint(1, len(D.GENDERS))
        return r.sample(D.GENDERS,random_length)
    elif field == 'top_size':
        random_length = r.randint(2, 7)
        return r.sample(D.TOP_SIZE, random_length)
    elif field == 'bottom_size':
        random_length = r.randint(2, 7)
        return r.sample(D.BOTTOM_SIZE, random_length)
    elif field == 'shoes_size':
        random_length = r.randint(2, 7)
        return r.sample(D.SHOES_SIZE, random_length)
    elif field == 'brands':
        random_length = r.randint(1, 1)
        return r.sample(D.BRANDS, random_length)
    else:
        return

# Функция folder_random_data генерирует полный объект folder для создания попки в соответствии с:
# name_length - длина поля Name
# name_type - тип символов в поле Name из словаря TYPES класса DataTypes
# user_id_length - длина поля User ID
# user_id_type - тип символов в поле User ID из словаря TYPES класса DataTypes
# Пример: folder_random_data(2, D.TYPES['cyrillic'], 1, D.TYPES['spec'])
def folder_random_data(name_length, name_type, user_id_length, user_id_type):
    return {
        'name': get_random_string(name_length, name_type),
        'user_id': get_random_string(user_id_length, user_id_type),
        'gender': get_random_list('gender'),
        'top_size': get_random_list('top_size'),
        'bottom_size': get_random_list('bottom_size'),
        'shoes_size': get_random_list('shoes_size'),
        'brands': get_random_list('brands')
        }
