def get_k_and_b(start, pos):
    end = [pos[0], pos[1]]
    num1 = start[0] - end[0]
    num2 = start[1] - end[1]
    if num1 == 0:
        k = 100000
    else:
        k = num2 / num1
    b = start[1] - (k * start[0])
    if abs(k) == 0.0:
        k = 0.00001
    return (k, b)


def get_sin(start, end):
    x_leg = end[0] - start[0]
    y_leg = end[1] - start[1]
    hypotenuse = (x_leg ** 2 + y_leg ** 2) ** 0.5
    sin = y_leg / hypotenuse
    return sin


def get_cos(start, end):
    x_leg = end[0] - start[0]
    y_leg = end[1] - start[1]
    hypotenuse = (x_leg ** 2 + y_leg ** 2) ** 0.5
    cos = x_leg / hypotenuse
    return cos


