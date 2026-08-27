import random

def hangman():
    """
    A simple text-based Hangman game where the player guesses a word one letter at a time.
    
    Features:
    - 5 predefined words to guess from
    - Maximum 6 incorrect guesses allowed
    - Console-based input/output
    - Interactive gameplay with clear feedback
    """
    
    # Predefined word list
    words = ["python", "hangman", "internship", "codealpha", "programming"]
    
    # Select a random word
    word = random.choice(words)
    word_length = len(word)
    guessed_word = ["_"] * word_length
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6
    
    print("=" * 50)
    print("🎮 WELCOME TO HANGMAN GAME 🎮")
    print("=" * 50)
    print(f"\nThe word has {word_length} letters.")
    print(f"You have {max_incorrect} incorrect guesses allowed.")
    print("\nGood luck! 🍀\n")
    
    # Main game loop
    while incorrect_guesses < max_incorrect and "_" in guessed_word:
        print(f"Word: {' '.join(guessed_word)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Incorrect guesses remaining: {max_incorrect - incorrect_guesses}")
        
        # Draw hangman stages
        draw_hangman(incorrect_guesses)
        
        # Get player input
        guess = input("\nGuess a letter: ").lower().strip()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single letter!")
            continue
        
        if guess in guessed_letters:
            print(f"⚠️  You already guessed '{guess}'. Try a different letter!")
            continue
        
        # Add guess to guessed letters
        guessed_letters.add(guess)
        
        # Check if guess is correct
        if guess in word:
            print(f"✅ Great! '{guess}' is in the word!")
            
            # Reveal guessed letters
            for i in range(word_length):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            print(f"❌ Sorry! '{guess}' is not in the word.")
            incorrect_guesses += 1
        
        print("-" * 50)
    
    # Game end conditions
    print("\n" + "=" * 50)
    if "_" not in guessed_word:
        print("🎉 CONGRATULATIONS! YOU WON! 🎉")
        print(f"The word was: {word}")
        print("=" * 50)
    else:
        print("😢 GAME OVER! YOU LOST! 😢")
        print(f"The word was: {word}")
        print("=" * 50)


def draw_hangman(incorrect_guesses):
    """
    Display the hangman figure based on the number of incorrect guesses.
    """
    stages = [
        """
           ------
           |    |
           |
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   \\|
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   \\|/
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   \\|/
           |    |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   \\|/
           |    |
           |   / \\
        --------
        """
    ]
    
    print(stages[incorrect_guesses])


def main():
    """
    Main function to run the Hangman game with replay option.
    """
    play_again = "yes"
    
    while play_again.lower() in ["yes", "y"]:
        hangman()
        play_again = input("\nDo you want to play again? (yes/no): ")
    
    print("\n🙏 Thanks for playing Hangman! See you next time! 🙏\n")


if __name__ == "__main__":
    main()
