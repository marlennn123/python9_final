import random
f_d = int(input('Томонку диапозонду жазыныз: '))
s_d = int(input('Жогорку диапозонду жазыныз: '))
random_number = random.randint(f_d, s_d)
count = 0

while True:
    cl_n = int(input(f'{f_d} жана {s_d} ортосундагы санды табыныз: '))
    count +=1
    if cl_n > random_number:
        print('Сиз жазган сан чон')
    elif cl_n < random_number:
        print('Сиз жазган сан кичине')
    elif cl_n == random_number:
        print(f'Куттуктайбыз! сиз {f_d} менен {s_d} ортосундагы санды {count} иретте таптыныз ')
        break