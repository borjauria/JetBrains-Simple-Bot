def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    # Remainders are the remains of dividing age by 3, 5 and 7.
    remainder3 = int(input('Enter the rest resulting from dividing your age by 3: > '))
    remainder5 = int(input('Enter the rest resulting from dividing your age by 5: > '))
    remainder7 = int(input('Enter the rest resulting from dividing your age by 7: > '))

    # Guess how old you are
    your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

    print(f"Your age is", your_age, "that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    # write your code here
    print("Why do we use methods? \n1. To repeat a statement multiple times.\n2. To decompose a program into several small subroutines.\n3. To determine the execution time of a program.\n4. To interrupt the execution of a program?")
    
    choose = input()

    while choose == 2:
        print('Completed, have a nice day!')
    else:
        print("error: Wrong answer!")

def end():
        print('Congratulations, have a nice day!')


greet('borjauria', '2020')
remind_name()
guess_age()
count()
test()
end()