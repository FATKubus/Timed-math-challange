import random as rd
import time

OPERATORS = ["//"]
Min_operand = 1
Max_operand = 20
Total_Problems = 10
def generate_problem():
    left = rd.randint(Min_operand, Max_operand)
    right = rd.randint(Min_operand, Max_operand)
    operator = rd.choice(OPERATORS)

    expr = str(left) + " " + operator  + " " + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
input("Press enter to start!")
print("--------------------")

start_time = time.time()

for i in range(Total_Problems):
    expr, answer = generate_problem()
    while True:
        guess =  input("Problem #" + str(i + 1)+ ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1
end_time = time.time()
total_time = end_time - start_time


print("--------------------")
print("U think that u're Elon Musk? You finished in", total_time, "seconds!")