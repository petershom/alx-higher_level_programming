Conditionals, Loops and Functions
This project contains some tasks for learning about conditionals, loops, and functions in Python.

Tasks To Complete
 0. Positive anything is better than negative nothing
0-positive_or_negative.py contains a Python script that will assign a random signed number to the variable number each time it is executed and print whether the number stored in the variable number is zero, positive or negative.
 1. The last digit
1-last_digit.py contains a Python script that will assign a random signed number to the variable number each time it is executed and print the last digit of the number stored in the variable number.
 2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game
2-print_alphabet.py contains a Python script that prints the ASCII alphabet, in lowercase, not followed by a new line.
 3. When I was having that alphabet soup, I never thought that it would pay off
3-print_alphabt.py contains a Python script that prints the ASCII alphabet (except q and e), in lowercase, not followed by a new line.
 4. Hexadecimal printing
4-print_hexa.py contains a Python script that prints all numbers from 0 to 98 in decimal and in hexadecimal (format: dec = hex, e.g.; 2 = 0x2).
 5. 00...99
5-print_comb2.py contains a Python script that prints numbers from 0 to 99 separated by a space and a comma and with a width of 2.
 6. Inventing is a combination of brains and materials. The more brains you use, the less material you need
6-print_comb3.py contains a Python script that prints all possible different combinations of two digits.
 7. islower
7-islower.py contains a function that checks for lowercase character.
 8. To uppercase
8-uppercase.py contains a function that prints a string in uppercase followed by a new line.
 9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important
9-print_last_digit.py contains a function that prints the last digit of a number.
 10. a + b
10-add.py contains a function that adds two integers and returns the result.
 11. a ^ b
11-pow.py contains a function that computes a to the power of b and return the value.
 12. Fizz Buzz
12-fizzbuzz.py contains a function that prints the numbers from 1 to 100 separated by a space.
 13. Insert in sorted linked list
13-insert_number.c contains a function in C that inserts a number into a sorted singly linked list.
 14. Smile in the mirror
100-print_tebahpla.py contains a Python script that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (z in lowercase and Y in uppercase) , not followed by a new line.
 15. Remove at position
101-remove_char_at.py contains a function that creates a copy of the string, removing the character at the position n (not the Python way, the “C array index”).
 16. ByteCode -> Python #2
102-magic_calculation.py contains a function def magic_calculation(a, b, c): that does exactly the same as the following Python bytecode:
  3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
