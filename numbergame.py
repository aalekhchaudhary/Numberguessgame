import random
print("Number Guessing Game!")
number = random.randint(1, 100)
attempts=0   
chances=8 
print("INSTRUCTIONS TO PLAY THE GAME")
print("1. You have maximum 8 chances to win the game\n2. You have to choose any number inbetween 1 to 100\n3. Game is very simple and fantastic")
print("Select a random number between 1 and 100.")
    
while(chances>=attempts):
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1

        if guess < number:
            print("SMALL NUMBER! Try again.")
        elif guess > number:
            print("LARGE NUMBER! Try again.")
        elif guess == number:
            print(f"Correct! You guessed the number in {attempts} attempts.")
    