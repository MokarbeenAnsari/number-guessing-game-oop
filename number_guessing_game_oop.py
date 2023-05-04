import random

class NumberGuessingGame:
    # This is constructor, which will initialize the properties
    def __init__(self, min_number=1, max_number=25, ) -> None:
        self.min_number = min_number
        self.max_number = max_number
        self.target_number = random.randint(min_number, max_number)
        self.attempt_count = 0
        self.game_active = True

    # This method will print the welcome message on the screen
    def display_wecome_message(self):
        print(f"Welcome to the Number Guessing Game!")
        print(f"I am thinking of a number between {self.min_number} and {self.max_number}.")

    # This method will take the input from user
    def get_user_input(self, prompt_message):
        return input(prompt_message)
    
    # This method will check the guessed number matched or not
    def guess_check(self, guess_number):
        if guess_number > self.target_number:
            print(f"Lower! Try a smaller number.")
        elif guess_number < self.target_number:
            print(f"Higher! Try a higher number.")
        else:
            print(f"Congratulations! You guessed the number correctly in {self.attempt_count} attempt!")
            self.attempt_count = 0
            self.game_active = False
            self.play_again()

    # This method will ask to play again or exit
    def play_again(self):
        choice = self.get_user_input("Do you want to play again? (yes or no): ")
        if choice.lower() == "yes":
            self.target_number = random.randint(self.min_number, self.max_number)
            self.game_active = True
        elif choice.lower() == "no":
            print("Thanks for playing! Goodbye!")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            self.play_again()

    # This is the main method, from here game will start
    def main(self):
        self.display_wecome_message()
        while self.game_active:
            try:
                user_guess = int(self.get_user_input(f"Enter your guess: "))
                self.attempt_count += 1
                self.guess_check(user_guess)
            except ValueError:
                print(f"Invalid input. Please enter a number.")

# Game will start from here
if __name__ == '__main__':
    game = NumberGuessingGame()
    game.main()
