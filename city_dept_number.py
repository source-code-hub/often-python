#!/usr/bin/env python
# File Name: dailysolution.py

"""
Assign number 1-7 to three departments in a city: Fire, Police, Sanitation.

Requirement:

- Each department should have a unique number
- Police should be an even number
- Fire + Police + Sanitation = 12
"""


def check_requirement(p, f, s):
    return p % 2 == 0 and p != f and p != s and s != f and p + f + s == 12


# Testable
def assign_number():
    numbers = []
    for f in range(1, 8):
        for p in range(1, 8):
            for s in range(1, 8):
                if check_requirement(p, f, s):
                    numbers.append({'Police': p, 'Fire': f, 'Sanitation': s})
    return numbers


def assign_number_1():
    numbers = []
    for p in range(1, 8):
        if p % 2 == 0:
            for f in range(1, 8):
                if p != f:
                    for n in range(1, 8):
                        if p != n and n != f and p + f + n == 12:
                            numbers.append({'Police': p, 'Fire': f, 'Sanitation': n})
    return numbers


if __name__ == "__main__":
    print(assign_number())
