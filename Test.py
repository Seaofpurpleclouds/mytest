def check(n):
    if (n < 2):  # compare number
        return (n % 2 == 0)
    return (check(n - 2))   # function call from a number minus 2


n = input('Введите число: ')  # please enter a number to check
if n.isdigit() == False:   # check if the string consisted of numbers
    print('Вы ввели не целое число!')
else:
    n = int(n)
    if (check(n) == True):    # check number
        print('Число четное!')
    else:
        print('Число нечетное!')
        
# данный способ хуже предоставленного, поскольку все невыполненные функции-рекурсии забивают стек.


#============================================================

class Fifo_bufer: # first way
    def __init__(self, long_n):
        self.bufer = [0] * long_n

    def buferUse(self, new_value):
        self.bufer = self.bufer[1:] + [new_value]#

first_fifo_bufer = Fifo_bufer(7)
first_fifo_bufer.buferUse(6)

print(first_fifo_bufer.bufer)

#=============================================================

class Fifo_bufer_two: # second way
    def __init__(self, long_n):
        self.bufer = [0] * long_n

    def buferUse(self, new_value):
        self.bufer.pop(0)
        self.bufer.append(new_value)
        

fifo = Fifo_bufer_two(5)
fifo.buferUse(5)
print(fifo.bufer)


#=================================================================

from collections import deque as dq

class Fifo_bufer_three: # thirt way
    def __init__(self, long_n):
        self.bufer = dq([0 for i in range(long_n)], maxlen=long_n)

    def buferUse(self, new_value):
        self.bufer.append(new_value)


fifo_three = Fifo_bufer_three(5)
fifo_three.buferUse(5)

print(fifo_three.bufer)

# В данном способе используется библиотека collections модуль deque, что создает список с максимлаьным заданным количеством элементов.


#================================================================


def bubleSort(nums): # Сортировка пузырьком. Выбрал ее потому что, на данный момент изучил только его.
    check = True
    while check:
        check = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                check = True
    return nums


random_list_of_nums = [5, 2, 1, 8, 4]  

print(bubleSort(random_list_of_nums))
