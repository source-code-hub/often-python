#!/usr/bin/env python
# File Name: robber_guard.py

import math

import matplotlib.pyplot as plt

# Robber
rx = -50  # Initial X Pos
ry = 35  # Initial Y Pos
rs = 4  # Speed

# Guard
gx = 35  # Initial X Pos
gy = 32  # Initial Y Pos
gs = 5  # Speed


class Person:
    def __init__(self, x_pos, y_pos, speed):
        self.x = x_pos
        self.y = y_pos
        self.speed = speed

    def run(self, towards_x, towards_y, t):
        a = math.atan2(self.x - towards_x, self.y - towards_y)
        d = self.speed * t
        self.x = self.x - d * math.sin(a)
        self.y = self.y - d * math.cos(a)
        return self.x, self.y

    def __str__(self):
        return str(self.get_pos())

    def get_pos(self):
        return math.floor(self.x), math.floor(self.y)

    def __eq__(self, other):
        return self.get_pos() == other.get_pos()


if __name__ == "__main__":
    rob = Person(rx, ry, rs)
    guard = Person(gx, gy, gs)
    crx, cry = rx, ry
    cgx, cgy = gx, gy
    # Labels
    plt.text(rx, ry, 'Robber')
    plt.text(gx, gy, 'Guard')
    plt.plot(0, 0, 'gs')
    plt.plot(-1, 0, 'gs')
    plt.plot(1, 0, 'gs')
    plt.text(-2.5, -1.5, 'Gate')
    # Start chase
    while True:
        x, y = guard.run(crx, cry, .1)
        plt.plot(x, y, 'b.')

        # Caught
        if guard == rob:
            plt.text(guard.x, guard.y, 'Caught')
            print("Robber Caught at: {}".format(guard))
            break
        crx, cry = rob.run(0, 0, .1)
        plt.plot(crx, cry, 'r.')

        # Escaped
        if math.floor(crx) <= 0 and math.floor(cry) <= 0:
            plt.text(rob.x, rob.y, 'Escaped')
            print("Robber Escaped")
            break
        print(rob, guard)
    plt.show()
