#  Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.

def key_to_val(**kwargs):
    start_dict = {}
    start_dict = kwargs
    print(start_dict)
    k = []
    v = []
    for key, value in start_dict.items():
        v.append(key)
        try:
            hash(value)
            k.append(value)
        except: k.append(str(value))
    print(dict(zip(k, v)))
            
 
    
key_to_val(a = "wsdasada", 
           b = 123, 
           c = "123", 
           d = [1,2,3])
