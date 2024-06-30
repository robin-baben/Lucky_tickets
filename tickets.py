def next(pred):
    '''
    функция перехода от n к n+1
    Принимает на вход массив значений A_n(k), возвращает массив значений A_n+1(k)
    '''

    l = len(pred)

    result = [1] * ((l + 9) // 2 + (l + 9) % 2)

    for i in range((l + 9) // 2 + (l + 9) % 2 - 1):
        result[i + 1] = result[i] + pred[i + 1]

        if i >= 9:
            result[i + 1] -= pred[i - 9]
        
    return result + result[:(l + 9) // 2][::-1]
    

def count_sum_n(n):
    '''
    Функция подсчета числа счасливых билетов, для билета длины 2n
    Принимает на вход n - длину половины билета
    Возвращает число счастливых билетов
    '''
    result = [1 for _ in range(10)] # массив значений A_1(k)

    for _ in range(n - 1):
        result = next(result) #реккурентно вычисляем массивы значений A_n(k)

    total = 0 #число счастливых вилетов
    
    for num in result:
        total += num ** 2 #подсчитываем число счастливых билетов

    return total


import time

n = 1 #длина половины билета
t = 0 # время работы программы

while (t < 60):

    start = time.time()
    count_next = count_sum_n(n)
    end = time.time()

    t = end - start
    print(t)

    n += 100
    '''
    Так как программа работает очень быстро при малых n,
    разумно n сначала увеличивать на 100, затем на 10,
    и когда время работы программы станет близким к одной минуте,
    тогда увеличивать n на единицу.
    '''


n -= 100

while (t < 60):

    start = time.time()
    count_sum_n(n)
    end = time.time()

    t = end - start
    print(t)
    n += 10

n -= 10

while (t < 60):

    start = time.time()
    count_sum_n(n)
    end = time.time()

    t = end - start
    print(t)
    n += 1


print(f"Максимальная длина билета {2*(n-1)}")

start = time.time()
count_l = count_sum_n(6 // 2)
end = time.time()

print(f"время работы программы для N=6 равно {(end-start) * 1000} милисекунд, число счастливых билетов равно {count_l}")

start = time.time()
count_l = count_sum_n(20 // 2)
end = time.time()

print(f"время работы программы для N=20 равно {(end-start) * 1000} милисекунд, число счастливых билетов равно {count_l}")

start = time.time_ns()
count_l = count_sum_n(50 // 2)
end = time.time_ns()

print(f"время работы программы для N=50 равно {(end-start) * 1000} милисекунд, число счастливых билетов равно {count_l}")

start = time.time()
count_l = count_sum_n(648 // 2)
end = time.time()

print(f"время работы программы для N=648 равно {end-start} секунд, число счастливых билетов равно {count_l}")


