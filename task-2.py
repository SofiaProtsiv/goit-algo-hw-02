from collections import deque


def is_palindrome(input_string):
    normalized_string = "".join(input_string.lower().split())
    
    char_deque = deque(normalized_string)

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True

test_strings = [
    "MaDaM",
    "Level",
    "Hello world",
    "R e f e r",
    "Python 3",
]

for test in test_strings:
    print(f"'{test}' є паліндромом: {is_palindrome(test)}")
