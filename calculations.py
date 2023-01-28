import numpy as np
from scipy.integrate import quad

# k(x) * u''(x) = f(x)
# u''(x) = -f(x)/k(x)
# u(0) +  u'(0) = gamma
# u'(0) = gamma - u(0)
# u(2) = u2
global gamma, u2
gamma, u2 = 20, 0


# Functions -f(x), k(x)
def fun_f(x):
    return -100 * x


def fun_k(x):
    if x < 0 or x > 2:
        return 0
    if x <= 1:
        return x + 1
    return 2 * x


# Function returns the ith element (basic function)
def e_i(i, x):
    return max(0, 1 - abs((x - i * h) / h))


# Function returns the derivative of the ith element (derivative of the base function)
def derivative_e_i(i, x):
    return 1 / h * (h * (i - 1) <= x) * (x < h * i) * (0 <= x) - 1 / h * (h * i <= x) * (x < h * (i + 1)) * (x <= 2)


# Function returns B(u, v)
def B(u, v, start, end):
    integral = quad(lambda x: derivative_e_i(u, x) * derivative_e_i(v, x), start, end)[0]
    return e_i(v, 0) * e_i(u, 0) - integral


# Function returns L(v)
def L(i, start, end):
    if end <= 1:
        integrals = quad(lambda x: fun_f(x) * e_i(i, x) / fun_k(x), max(0, start), min(1, end))[0]
    elif start >= 1:
        integrals = quad(lambda x: fun_f(x) * e_i(i, x) / fun_k(x), max(1, start), min(2, end))[0]
    else:
        integrals = quad(lambda x: fun_f(x) * e_i(i, x) / fun_k(x), max(0, start), min(1, end))[0] \
                    + quad(lambda x: fun_f(x) * e_i(i, x) / fun_k(x), max(1, start), min(2, end))[0]

    return integrals + gamma * e_i(i, 0)


# Functions find ranges for integrals
def B_range(i, j):
    if abs(i - j) == 1:
        start = 2. * max(0, min(i, j) / n)
        end = 2. * min(1, max(i, j) / n)
        return start, end

    start = 2. * max(0, (i - 1) / n)
    end = 2. * min(1, (i + 1) / n)
    return start, end


def L_range(i):
    start = 2. * max(0, (i-1) / n)
    end = 2. * min(1, (i + 1) / n)
    return start, end


def solver(n):
    first_matrix_B = [[B(i, j, B_range(i, j)[0], B_range(i, j)[1]) for j in range(n + 1)] for i in range(n)]
    first_matrix_B.append([0.0 if i < n else 2.0 for i in range(n + 1)])
    matrix_B = np.array(first_matrix_B)

    first_matrix_L = [L(i, L_range(i)[0], L_range(i)[1]) for i in range(n)]
    first_matrix_L.append(u2)
    vector_L = np.array(first_matrix_L).T

    u_solution = np.linalg.solve(matrix_B, vector_L)

    return u_solution


def create_solution(parameter):
    global n, h
    n = parameter
    h = 2 / n

    solX = [h * i for i in range(n + 1)]
    solY = solver(n)

    return solX, solY
