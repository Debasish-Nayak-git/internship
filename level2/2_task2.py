import random
class GuessingGame:
    def __init__(self,low,high):
        self.low=low
        self.high=high
        self.number=random.randint(self.low,self.high)
    
    def play(self):
        guess=None
        while guess != self.number:
            guess=int(input("Enter your guess:"))
            if guess >self.number:
                print("Too high")
            elif guess < self.number:
                print("Too low")
            else:
                print("You guess the correct number")

game= GuessingGame(1,100)
game.play()