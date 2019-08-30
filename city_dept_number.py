#!/usr/bin/env python
# File Name: city_dept_number.py

"""
Assign number 1-7 to three departments in a city: Fire, Police, Sanitation.

Requirement:

- Each department should have a unique number
- Police should be an even number
- Fire + Police + Sanitation = 12
"""


def check_requirement(p, f, s):
    return p % 2 == 0 and p != f and p != s and s != f and p + f + s == 12


# First go!
def assign_number():
    numbers = []
    for f in range(1, 8):
        for p in range(1, 8):
            for s in range(1, 8):
                if check_requirement(p, f, s):
                    numbers.append({'Police': p, 'Fire': f, 'Sanitation': s})
    return numbers


def rec_combination(combination, index, elements):
    if index == len(elements):
        print(combination)
    else:
        combination.append(elements[index])
        rec_combination(combination, index+1, elements)

        combination.remove(elements[index])
        rec_combination(combination, index + 1, elements)


def ncr_combination(elements, c_index, combination, index, r):
    if c_index == r:
        yield combination
        return
    if index >= len(elements):
        return
    combination[c_index] = elements[index]
    yield from ncr_combination(elements, c_index + 1, combination, index + 1, r)
    yield from ncr_combination(elements, c_index, combination, index + 1, r)


if __name__ == "__main__":
    print(*assign_number(), sep="\n")
    print("\nPrint a combination of r element out of n\n")
    arr = [1, 2, 3, 4, 5, 6, 7]
    comb = []
    r = 3
    n = len(arr)
    data = [0, 0, 0]
    for c in ncr_combination(arr, 0, data, 0, r):
        print(c)