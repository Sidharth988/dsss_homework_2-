import unittest
from math_quiz import Random_integer, Random_operation, Operation


class TestMathGame(unittest.TestCase):

    def test_Random_integer(self):
        # Test random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = Random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_Random_operation(self):
        # check if random operation generated are +, -, *
        for _ in range(1000):
             rand_op = Random_operation()
             self.assertTrue( rand_op == '*' or rand_op=='+'or rand_op == '-')
        

    def operation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7), (5, 2, '-', '5 - 2', 3), (5, 2, '*', '5 * 2', 10)
                
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                PROBLEM, ANSWER = Operation(num1, num2, operator)
                self.assertTrue(expected_problem== PROBLEM and expected_answer == ANSWER)

if __name__ == "__main__":
    unittest.main()
