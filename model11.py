# Интроспекция
import inspect
import sys


def introspection_info(obj):
    # Получаем тип объекта
    obj_type = type(obj).__name__

    # Получаем атрибуты объекта
    attributes = [attr for attr in dir(obj) if not attr.startswith('__')]

    # Получаем методы объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]

    # Получаем модуль объекта
    module = inspect.getmodule(obj)

    # Сбор информации об объекте в словарь
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module,
        'id': id(obj)  # добавим id объекта как дополнительное свойство
    }

    return info

# Пример использования функции:
number_info = introspection_info(42)
print(number_info)