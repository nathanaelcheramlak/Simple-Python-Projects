from random import randint

def generate_random_number():
    num = randint(1000, 9999)
    number_list = []
    for i in str(num):
        if i not in number_list and i != '0':
            number_list.append(i)
    while len(number_list) < 4:
        x = randint(1, 9)
        x = str(x)
        if x not in number_list:
            number_list.append(x)
    return number_list
