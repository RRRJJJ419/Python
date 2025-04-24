'''
file = open("myfile.txt", encoding="utf-8")
print(file.read())
-------------------------------------------------
with open("myfile.txt") as f:
    all_content = f.read()
    print(all_content)
-------------------------------------------------
with open("myfile.txt", mode="a") as f:
    f.write("\nLearning Python.")
-------------------------------------------------
import os
os.rmdir("newfloder")
-------------------------------------------------
'''
import random

secret = random.randint(1, 100)
min_value = 1
max_value = 100
print(secret)

while True:
    guess = input(f"Make your guess (between {min_value} and {max_value}):")
    if int(guess) < min_value or int(guess) > max_value:
        print("Your guess is not in range")
        continue
    if int(guess) == secret:
        print(f"The secret is {secret}")
        break
    elif int(guess) < secret:
        min_value = int(guess)
    elif int(guess) > secret:
        max_value = int(guess)
