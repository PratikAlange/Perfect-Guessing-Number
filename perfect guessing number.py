# Perfect guessing number


import random
a=random.randint(1,100)
attempt,num=0,0
while num!=a:
    num=int(input('Enter number:'))
    if num>a:
        print("It's too high!")
    elif num<a:
        print("It's too low!")
    attempt+=1
print(f'You guessed the number:{a} in {attempt} attempts')
