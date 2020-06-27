###################################################################################
# this a program to find the single properoship function's solution
# |    /                                     
# |   /                                     
# |  /
# |_/________________________________ x
# |/
#

import math


def f(x):
    return math.sin(x)

# find the solution to f(x) = y
def equation(x, y):
    return f(x) - y

def find_solution(a, b, y):
    l_value = equation(a, y)
    r_value = equation(b, y)

    if (abs(l_value) < 0.0001):
        return a
    if (abs(r_value) < 0.0001):
        return b

    m = (a + b) / 2
    m_value = equation(m, y)

    if (m_value * l_value < 0):
        return find_solution(a, m, y)
    elif (m_value * r_value < 0):
        return find_solution(m, b, y)
    else:
        print("left and right have identical sign")

results = find_solution(0.1, 1.5, 0.5)
print("answer", results)