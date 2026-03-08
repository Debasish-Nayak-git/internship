import random
class GuessingGame:
    def __init__(self):
        self.number=random.randint(1,100)
    
    def play(self):
        guess=None
        while guess != self.number:
            guess=int(input("Enter your guess:"))
            if guess >self.number:
                print("Too high")
            elif guess < self.number:
                print("Too low")
            else:
                print("correct guess")

game= GuessingGame()
game.play()