# Jason Reeves
# CS 415 Tree Object File
# A class to represent trees (real trees, not CS trees).

import math


class Tree:
    # Initialization function
    # - name: Name of tree
    # - x: X-coordinate of tree (can be string or float)
    # - y: Y-coordinate of tree (can be string or float)
    def __init__(self, name, x, y):
        self.name = name
        self.x = float(x)
        self.y = float(y)

    # Find the distance between this tree
    # and a given point (x, y).
    # - x: X-coordinate of given point (must be number)
    # - y: Y-coordinate of given point (must be number)
    def get_distance(self, x, y):
        # Use the Pythagorean Theorem to find the distance
        # If a^2 + b^2 = c^2, then c = sqrt(a^2 + b^2)!

        # Here, a is the x difference, and
        # b is the y difference
        a_sq = (x - self.x) ** 2
        b_sq = (y - self.y) ** 2
        return math.sqrt(a_sq + b_sq)
