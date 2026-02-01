import random


def generate_questions():
    print("=== Math Addition Practice ===")
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
    if score == 5:
        print("Perfect score! Amazing!")
    elif score >= 3:
        print("Good job! Keep practicing!")
    else:
        print("Don't give up! Practice makes perfect!")


if __name__ == "__main__":
    generate_questions()
