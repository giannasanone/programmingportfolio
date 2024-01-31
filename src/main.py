#main.py
#main.py
import random

print(str("Welcome To The Guessing Game"));
print(str("You will have 3 chance to guess the number between 1 and 100"));

number = random.randint(1, 100);
for _ in range(3):
  test=int(input("Guess the number: "));
  if test == number:
      print("You guessed the number!")
      break
  else:
      print("You did not guess the number")

print("The number was " + str(number))
