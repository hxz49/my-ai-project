import os
import random

HIGH_SCORE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "high_score.txt")


def load_high_score():
    try:
        with open(HIGH_SCORE_FILE, "r") as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 0


def save_high_score(score):
    with open(HIGH_SCORE_FILE, "w") as f:
        f.write(str(score))


def generate_questions():
    print("=== Math Addition Practice ===")
    high_score = load_high_score()
    print(f"Current high score: {high_score}/5")
    print("Answer the 5 addition questions below. Good luck!\n")

    score = 0

    for i in range(1, 6):
        a = random.randint(10, 999)
        b = random.randint(10, 999)
        correct_answer = a + b

        user_input = input(f"Question {i}: {a} + {b} = ")

        try:
            if int(user_input) == correct_answer:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong. The answer is {correct_answer}.\n")
        except ValueError:
            print(f"Invalid input. The answer is {correct_answer}.\n")

    print(f"=== You got {score}/5 correct! ===")
    if score > high_score:
        save_high_score(score)
        print(f"New high score! {score}/5!")
    if score == 5:
        print("Perfect score! Amazing!")
    elif score >= 3:
        print("Good job! Keep practicing!")
    else:
        print("Don't give up! Practice makes perfect!")


if __name__ == "__main__":
    generate_questions()
