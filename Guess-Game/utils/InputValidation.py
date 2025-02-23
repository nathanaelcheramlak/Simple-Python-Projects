def input_check(guess):
    guess_list = []
    unique_list = []
    for i in guess:
        if i not in unique_list:
            unique_list.append(i)
    for num in guess:
        guess_list.append(num)

    if unique_list != guess_list:
        check = False
    else:
        check = True
    return check

def length_checker(guess):
    num = []
    for i in guess:
        num.append(i)
    if len(guess) == 4 and '0' not in num:
        check = True
    else:
        check = False
    return check

def number_checker(guess):
    num_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
    list_true = []
    list_false = []
    for i in guess:
        if i in num_set:
            list_true.append(i)
        else:
            list_false.append(i)
    if len(list_false) == 0:
        check = True
    else:
        check = False
    return check

def authentication(guess):
    length = length_checker(guess)
    in_check = input_check(guess)
    num_only = number_checker(guess)
    if length and in_check and num_only:
        check = True
    else:
        check = False
    return check

def command_checker(command):
    while command > 4 or command < 1:
        command = int(input("---->"))
    return command
