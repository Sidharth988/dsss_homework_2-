import random

def Random_integer(min, max):
    """
    function takes parameters min&max 
    and return random integer (min,max)

    """
    return random.randint(min, max)

def Random_operation():
    """ 
    This function randomly chooses an operation among '+','-','*'
    
    """
    return random.choice(['+', '-', '*'])


def Operation(Num_1, Num_2, o):
    """
    function takes parameters Num_1, Num_2,o
    computes operation and returns 2 variables
    1. p: The string containing the problem
    2. a: The result
    """
    p = f"{Num_1} {o} {Num_2}"
    if o == '+': 
        a = Num_1 + Num_2
    elif o == '-': 
        a = Num_1 - Num_2
    else: 
        a = Num_1 * Num_2
    return p,a

def math_quiz():
    
    Score = 0
    t_q = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        Num_1 = Random_integer(1, 10)
        Num_2 = Random_integer(1, 54)
        o = Random_operation()
        PROBLEM, ANSWER = Operation(Num_1, Num_2, o)
        print(f"\nQuestion: {PROBLEM}")
        try:
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)  # Try converting the input to a int
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        else:
            print(f"Valid input! You entered: {useranswer}")
        

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            Score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {Score}/{t_q}")

if __name__ == "__main__":
    math_quiz()
