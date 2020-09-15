"""
Author: Aidan Shannon
Program: average_scores.py

program that takes multiple inputs and averages scores
to format and return an output
"""


def average():
    score1 = int(input("Enter your first grade: "))
    score2 = int(input("Enter your second grade: "))
    score3 = int(input("Enter your third grade: "))
    return (score1 + score2 + score3) / 3


if __name__ == '__main__':
    lastName = input("Enter your last name: ")
    firstName = input("Enter your first name: ")
    age = input("Enter your age: ")
    average_scores = average()
    print("{}, {} Age: {} Average Grade: {}".format(lastName, firstName, age, average_scores))
