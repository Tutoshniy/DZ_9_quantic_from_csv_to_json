def solve_equation(a, b, c=0):
    descrim = b**2 - 4 * a * c
    if descrim < 0:
        return None
    elif descrim == 0:
        return -b / (2 * a)
    elif descrim > 0:
        root1 = (-b - (descrim ** 0.5)) / (2 * a)
        root2 = (-b + (descrim ** 0.5)) / (2 * a)
        return root1, root2


if __name__ == '__main__':
    print(solve_equation(1, 2, 3))
