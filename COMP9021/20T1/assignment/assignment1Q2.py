from random import randint


def tranform(number, list):
    if number == 0:
        c = 'Ace'
        list.append(c)
    elif number == 1:
        c = 'King'
        list.append(c)
    elif number == 2:
        c = 'Queen'
        list.append(c)
    elif number == 3:
        c = 'Jack'
        list.append(c)
    elif number == 4:
        c = 10
        list.append(c)
    else:
        c = 9
        list.append(c)


def letter_to_number(number, list):
    if number == 'Ace':
        c = 0
        list.append(c)
    elif number == 'King':
        c = 1
        list.append(c)
    elif number == 'Queen':
        c = 2
        list.append(c)
    elif number == 'Jack':
        c = 3
        list.append(c)
    elif number == 10:
        c = 4
        list.append(c)
    else:
        c = 5
        list.append(c)


def identify(count_new_list, replace):
    if 5 in count_new_list:
        print('It is a Five of a kind')
    elif 4 in count_new_list:
        print('It is a Four of a kind')
    elif 3 in count_new_list and 2 in count_new_list:
        print('It is a Full house')
    elif replace == ['Ace', 'King', 'Queen', 'Jack', 10] or replace == ['King', 'Queen', 'Jack', 10, 9] or replace == [
        10, 'Jack', 'Queen', 'King', 'Ace'] or replace == [9, 10, 'Jack', 'Queen', 'King']:
        print('It is a Straight')
    elif 3 in count_new_list and 1 in count_new_list:
        print('It is a Three of a kind')
    elif count_new_list.count(2) == 1:
        print('It is a One pair')
    elif 2 in count_new_list:
        count_new_list.remove(2)
        if 2 in count_new_list:
            print('It is a Two pair')
    else:
        print('It is a Bust')


def play():
    dial = []
    for i in range(0, 5):
        a = randint(0, 5)
        dial.append(a)
    dial.sort()
    replace = []
    for n in dial:
        tranform(n, replace)
    replace.insert(0, 'The roll is:')
    for j in replace[:-1]:
        print(j, end=' ')
    print(replace[-1])
    replace.remove('The roll is:')
    count_list = ['Ace', 'King', 'Queen', 'Jack', 10, 9]
    count_new_list = []
    for num in count_list:
        time = replace.count(num)
        count_new_list.append(time)
    identify(count_new_list, replace)
    s = 1
    while s:
        count = 0
        remain = input('Which dice do you want to keep for the second roll? ')
        if str(remain) == 'all' or str(remain) == 'All':
            return print('Ok, done.')
        words = remain.split()
        temp_list = []
        for word in words:
            if word == '9' or word == '10':
                word = int(word)
                temp_list.append(word)
            else:
                temp_list.append(word)
        for j in temp_list:
            if j not in replace:
                print('That is not possible, try again!')
                break
            else:
                count += 1
        if count == len(temp_list):
            s = 0
    words = remain.split()
    if len(words) == 5:
        return print('Ok, done.')
    num_list = []
    for word in words:
        big = word.capitalize()
        if big == '9' or big == '10':
            big = int(big)
        num_list.append(big)
        letter_to_number(big, num_list)
        num_list.remove(big)
    for times in range(0, 5 - len(words)):
        add_number = randint(0, 5)
        num_list.append(add_number)
    num_list.sort()
    loop = 0
    while loop < 5:
        tranform(num_list[0], num_list)
        num_list.remove(num_list[0])
        loop += 1
    num_list.insert(0, 'The roll is:')
    for j in num_list[:-1]:
        print(j, end=' ')
    print(num_list[-1])
    num_list.remove('The roll is:')
    example = ['Ace', 'King', 'Queen', 'Jack', 10, 9]
    count_new_list = []
    for num in example:
        time = num_list.count(num)
        count_new_list.append(time)
    identify(count_new_list, num_list)
    s = 1
    while s:
        count = 0
        remain = input('Which dice do you want to keep for the third roll? ')
        if str(remain) == 'all' or str(remain) == 'All':
            return print('Ok, done.')
        words = remain.split()
        temp_list = []
        for word in words:
            if word == '9' or word == '10':
                word = int(word)
                temp_list.append(word)
            else:
                temp_list.append(word)
        for j in temp_list:
            if j not in replace:
                print('That is not possible, try again!')
                break
            else:
                count += 1
        if count == len(temp_list):
            s = 0
    words = remain.split()
    if len(words) == 5:
        return print('Ok, done.')
    num_list = []
    for word in words:
        big = word.capitalize()
        num_list.append(big)
        if big == '9' or big == '10':
            big = int(big)
        letter_to_number(big, num_list)
        num_list.remove(str(big))
    for times in range(0, 5 - len(words)):
        add_number = randint(0, 5)
        num_list.append(add_number)
    num_list.sort()
    loop = 0
    while loop < 5:
        tranform(num_list[0], num_list)
        num_list.remove(num_list[0])
        loop += 1
    num_list.insert(0, 'The roll is:')
    for j in num_list[:-1]:
        print(j, end=' ')
    print(num_list[-1])
    num_list.remove('The roll is:')
    example = ['Ace', 'King', 'Queen', 'Jack', 10, 9]
    count_new_list = []
    for num in example:
        time = num_list.count(num)
        count_new_list.append(time)
    identify(count_new_list, num_list)


# REPLACE PASS ABOVE WITH YOUR CODE


def simulate(n):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    for i in range(n):
        dial = []
        for j in range(0, 5):
            ran = randint(0, 5)
            dial.append(ran)
        dial.sort()
        replace = []
        for m in dial:
            tranform(m, replace)
        count_list = ['Ace', 'King', 'Queen', 'Jack', 10, 9]
        count_new_list = []
        for num in count_list:
            time = replace.count(num)
            count_new_list.append(time)
        if 5 in count_new_list:
            a += 1
        elif 4 in count_new_list:
            b += 1
        elif 3 in count_new_list and 2 in count_new_list:
            c += 1
        elif replace == ['Ace', 'King', 'Queen', 'Jack', 10] or replace == ['King', 'Queen', 'Jack', 10,
                                                                            9] or replace == [
            10, 'Jack', 'Queen', 'King', 'Ace'] or replace == [9, 10, 'Jack', 'Queen', 'King']:
            d += 1
        elif 3 in count_new_list and 1 in count_new_list:
            e += 1
        elif count_new_list.count(2) == 1:
            f += 1
        elif 2 in count_new_list:
            count_new_list.remove(2)
            if 2 in count_new_list:
                g += 1
    print('Five of a kind : ', '%.2f' % (a / n * 100), '%', sep='')
    print('Four of a kind : ', '%.2f' % (b / n * 100), '%', sep='')
    print('Full house     : ', '%.2f' % (c / n * 100), '%', sep='')
    print('Straight       : ', '%.2f' % (d / n * 100), '%', sep='')
    print('Three of a kind: ', '%.2f' % (e / n * 100), '%', sep='')
    print('Two pair       : ', '%.2f' % (g / n * 100), '%', sep='')
    print('One pair       : ', '%.2f' % (f / n * 100), '%', sep='')
    # REPLACE PASS ABOVE WITH YOUR CODE

# DEFINE OTHER FUNCTIONS
