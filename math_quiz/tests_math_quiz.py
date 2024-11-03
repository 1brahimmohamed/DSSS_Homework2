import unittest
from math_quiz import generate_random_integer, generate_random_operator, create_problem_and_answer


class TestMathGame(unittest.TestCase):

    def test_random_integer_within_range(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)         # Check if the random number is within the range

    def test_random_operator_is_valid(self):
        # Define valid operators and test if random operator is within the valid operators
        valid_operators = ['+', '-', '*']
        for _ in range(1000):
            operator = generate_random_operator()
            self.assertIn(operator, valid_operators)            # Check if the random operator is valid

    def test_problem_and_answer_are_correct(self):
        # Define test cases

        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (5, 2, '-', '5 - 2', 3),
            (5, 2, '*', '5 * 2', 10),
            (0, 0, '+', '0 + 0', 0),
            (0, 0, '-', '0 - 0', 0),
            (0, 0, '*', '0 * 0', 0),
            (10, 5, '+', '10 + 5', 15),
            (10, 5, '-', '10 - 5', 5),
            (10, 5, '*', '10 * 5', 50)
        ]

        # Test if the problem and answer are correct for each test case
        for first_number, second_number, operator, expected_problem, expected_answer in test_cases:
            problem, answer = create_problem_and_answer(first_number, second_number, operator)
            self.assertEqual(problem, expected_problem)     # Check if the problem is correct
            self.assertEqual(answer, expected_answer)       # Check if the answer is correct


if __name__ == "__main__":
    unittest.main()
