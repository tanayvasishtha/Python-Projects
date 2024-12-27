import random
import time

OPERATORS =["+","-","*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left= random.randint(MIN_OPERAND,MAX_OPERAND)
    right= random.randint(MIN_OPERAND,MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer=eval(expr)
    return expr, answer

wrong=0
input("Press Enter to start the challenge!")
print("____________________________________________________")
print("You have 10 seconds to solve each problem.")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess=input("Problem #" + str(i+1) + ":" + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("____________________________________________________")
print("Nice job! You got", TOTAL_PROBLEMS - wrong, "out of", TOTAL_PROBLEMS, "problems correct.")
print("Total time:", total_time, "seconds")