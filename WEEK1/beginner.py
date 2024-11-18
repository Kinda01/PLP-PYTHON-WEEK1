#quetion two
def personalized_greeting():
    # Ask for the user's name and favorite color
    name = input("What is your name? ")
    color = input("What is your favorite color? ")
    
    # Print a personalized greeting
    print(f"Hello, {name}! Your favorite color, {color}, is awesome! 🎨")

# Run the function
personalized_greeting()

#question two
def quiz_game():
    # List of questions and answers
    questions = [
        {"question": "What is the capital of France?", "options": ["a) London", "b) Paris", "c) Rome"], "answer": "b"},
        {"question": "What does CPU stand for?", "options": ["a) Central Processing Unit", "b) Computer Personal Unit", "c) Central Processor Unit"], "answer": "a"},
        {"question": "Which programming language is known for its snake mascot?", "options": ["a) Java", "b) C++", "c) Python"], "answer": "c"},
    ]
    
    score = 0
    
    # Loop through each question
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer (a/b/c): ").lower()
        
        if answer == q["answer"]:
            print("Correct! 🎉")
            score += 1
        else:
            print("Oops, that's incorrect. 😢")
    
    # Display the final score
    print(f"\nYou got {score} out of {len(questions)} questions right!")

# Run the function
quiz_game()
#Question 3
import random

def random_joke():
    # List of jokes
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐞",
        "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings. 😢",
        "Why do Python programmers prefer snake_case? Because they can't CSharp. 🐍",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem! 💡"
    ]
    
    # Randomly select and print a joke
    joke = random.choice(jokes)
    print(joke)

# Run the function
random_joke()
