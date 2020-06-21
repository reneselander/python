#Program for testing multiplication skills, by René Selander 6/2020.

import random

from random import randrange

queries = 0

correct = 0

not_correct = 0

total = 10

for i in range(1, 11):

     num_1 = random.randrange(0, 11)

     num_2 = random.randrange(0, 11)

     result = (num_1 * num_2)

     while True:

         try:

             a = int(input(f'What is {num_1} times {num_2}? '))

             queries + 1             

             if a == result:

                correct = correct + 1

                print(f'Correct!')


             elif a != result:                

                not_correct = not_correct + 1

                print(f'Not correct (correct answer is {result})')


             else:

                not_correct = not_correct + 1

                print(f'Not correct! {not_correct}')


             break


         except ValueError:

                print("You did not enter an answer.")


         except KeyboardInterrupt:

                print("You stopped the program.")


print(f'\n* * * RESULT * * *\nNot correct = {not_correct}\nCorrect = {correct}\nTotal score = {correct}({total})')