#Program for testing multiplication skills, by René Selander 6/2020.

import random #Import of the module that generates raandom numbers.

from random import randrange

queries = 0

correct = 0

not_correct = 0

total = 10 # Variable that states maximum correct answers.

for i in range(1, 11): #This loop will repeat the question 10 times.

     num_1 = random.randrange(0, 11) #This will generate a number between 0 and 10.

     num_2 = random.randrange(0, 11) #This will generate a number between 0 and 10.

     result = (num_1 * num_2) #This will multiply the random generated numbers.

     while True:

         try:

             a = int(input(f'What is {num_1} times {num_2}? ')) #Here the user will be asked what a number times another number will be.

             queries + 1 #This will count the number of questions asked.

             if a == result:

                correct = correct + 1 #This will count the correct answers.

                print(f'Correct!')

             else:

                not_correct = not_correct + 1 # This counts all the not correct answers.

                print(f'Not correct (correct answer is {result})')

             break

         except ValueError: #If the user enters a non integer or nothing, the respond will be what the next line says.

                print("You did not enter an answer.")

         except KeyboardInterrupt: #If the user hits CTRL + C, the program should stop (depending on the enviroment).

                print("You stopped the program.")

#Next line shows the total result for the user.
print(f'\n* * * RESULT * * *\nNot correct = {not_correct}\nCorrect = {correct}\nTotal score = {correct} of {total} which is equal to {correct/10*100}%')
