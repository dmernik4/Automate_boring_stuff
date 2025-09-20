# myMultiplicationQuiz.py
# Multiplication quiz for numbers from 0 - 10 (without using pyinputplus)

import random, time

numberOfQuestions = 10
correctAnswers = 0
totalTime = 0

for questionNumber in range(numberOfQuestions):
    # Pick two random numbers
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)

    incorrectAnswers = 0

    prompt = "#%s: %s x %s = " % (questionNumber + 1, num1, num2)

    while True:

        startTime = time.time()
        answer = input(prompt)
        endTime = time.time()

        # Check if the answer is correct
        if int(answer) == num1 * num2:
            if (endTime - startTime) > 8:
                print("Out of time!")
                break
            else:
                print("Correct!")
                correctAnswers += 1
                break
        elif incorrectAnswers < 2:
            print("Incorrect! Try again.")
            incorrectAnswers += 1
        else:
            print("Incorrect! The correct answer is %s." % (num1 * num2))
            incorrectAnswers = 0
            break

    totalTime += endTime - startTime
    time.sleep(1)  # Brief pause to let user see the result.

print("Score: %s / %s" % (correctAnswers, numberOfQuestions))
print("Total time taken: %.2f seconds" % totalTime)
