import random


def generate_random_integer(min_value, max_value):
    """
    Generate a random integer between min_value and max_value (inclusive).

    :param min_value: Minimum value for the random integer.
    :param max_value: Maximum value for the random integer.
    :return: Random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)


def generate_random_operator():
    """
    Generate a random operator from the list ['+', '-', '*'].

    :return: Random operator.
    """
    return random.choice(['+', '-', '*'])


def create_problem_and_answer(first_number, second_number, operator):
    """
    Create a math problem and calculate the answer based on the given operator.

    :param first_number: First number.
    :param second_number: Second number.
    :param operator: Operator for the math problem.
    :return: Tuple containing the problem as a string and the answer as an integer.
    """

    # Create the math problem
    problem = f"{first_number} {operator} {second_number}"

    # Calculate the answer based on the operator provided
    if operator == '+':
        answer = first_number + second_number
    elif operator == '-':
        answer = first_number - second_number
    else:
        answer = first_number * second_number

    return problem, answer


def math_quiz():
    """
    Main function to run the math quiz game.
    """

    # Initialize variables
    score = 0
    total_number_of_questions = 5  # Number of questions in the quiz

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # Loop through the total number of questions and ask the user to solve each problem
    for _ in range(total_number_of_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        problem, correct_answer = create_problem_and_answer(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        # use try-except block to handling invalid inputs like strings, etc.
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == correct_answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {correct_answer}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Display the final score to the user
    print(f"\nGame over! Your score is: {score}/{total_number_of_questions}")


if __name__ == "__main__":
    math_quiz()
