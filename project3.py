import random
import time


OPERATORS = ['+', '-', '*']
MIN_OPEREND = 3
MAX_OPEREND = 12
TOTAL_PROBLOMS = 10

def generate_porblem():
    left =random.randint(MIN_OPEREND, MAX_OPEREND)
    right = random.randint(MIN_OPEREND, MAX_OPEREND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " "  + str(right) 
    answer = eval(expr)
    return expr, answer


wrong = 0
input("Prss enter to start!")
print('---------------------')

start_time =time.time()

for i in range(TOTAL_PROBLOMS):
    expr, answer = generate_porblem()
    while True :
        guess = input('Problom # ' + str(i + 1) + ': ' + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)


print('---------------------')
print('Nice work! You finished in', total_time, 'seconds!')
