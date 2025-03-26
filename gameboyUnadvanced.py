import random
import time

#Roulette game where you guess a number between 1 and 10. Keeps guessing until you get it right.
def roulette():
  random.seed(10)
  correct = random.randint(1, 10)
  guess = int(input("Guess a number between 1 and 10:"))
  while True: 
    if guess == correct:
      print("You Win!")
      break
    else:
      print("Wrong! Guess again!")
      guess = int(input("Guess a number between 1 and 10:"))

#Math Quiz where it asks you what the usm of 2 numbers is. Keeps guessing until you get it.
def mathQuiz():
  random.seed(10)
  firstNumber = random.randint(1,10)
  secondNumber = random.randint(1,10)
  correct = firstNumber + secondNumber
  print(f"What is {firstNumber} + {secondNumber}?")
  guess = int(input())
  while True:
    if guess == correct:
      print("You Win!")
      break
    else:
      print("Wrong! Guess again!")
      guess = int(input(f"What is {firstNumber} + {secondNumber}?"))

#Game in which you wait 5 seconds.
def waitingGame():
  time.sleep(5)
  print("You win!")

#Game Selector
while True:
  print("Select a Game!")
  print("1. Roulette")
  print("2. Math Quiz")
  print("3. The Waiting Game")
  print("4. Quit")

  number = int(input(""))

  if number == 1:
    roulette()
  elif number == 2:
    mathQuiz()
  elif number == 3:
    waitingGame()
  elif number == 4:
    break

 























