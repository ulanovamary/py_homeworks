'''
def int_func(*args: str):
    data = str.capitalize(*args)
    return data


print(int_func('data'))

'''
def int_func(sent):
    sent = sent.split(' ')
    new_sent = []
    for itm in sent:
        new_sent.append(itm.capitalize())
    return new_sent


sent = 'hello my friend'
print(int_func(sent))
