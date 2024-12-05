# Интроспекция

def introspection_info(obj):
    info = {}

    # Определяем тип объекта
    info['type'] = str(type(obj)).split("'")[1]  # Получаем только имя типа

    # Определяем атрибуты объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    info['attributes'] = attributes

    # Определяем методы объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    info['methods'] = methods

    # Определяем модуль, к которому принадлежит объект
    info['module'] = obj.__module__

    # Возвращаем собранную информацию
    return info

# Пример работы функции
number_info = introspection_info(42)
print(number_info)