import random

#for의 loop 횟수 x 1000원 = 로또 가격
for _ in range(5):
    lotto_numbers = range(1,46)
    my_numbers = random.sample(lotto_numbers, 6)
    my_numbers.sort()
    print(my_numbers)