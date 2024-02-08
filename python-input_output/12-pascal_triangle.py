#!/usr/bin/python3
""" contains the pascal_triangle function """


def pascal_triangle(a):
    """ returns the pascal triangle of a """
    if a <= 0:
        return []
    p_t = [[] for x in range(a)]
    p_t[0] = [1]
    if a > 1:
        p_t[1] = [1, 1]
    if a > 2:
        for i in range(2, a):
            p_t[i].append(1)
            for j in range(i - 1):
                p_t[i].append(p_t[i - 1][j] + p_t[i - 1][j + 1])
            p_t[i].append(1)
    return p_t
