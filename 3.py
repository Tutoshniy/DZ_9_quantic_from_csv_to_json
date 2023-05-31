import csv


def find_quadratic_from_file(func):
    def wrapper(file_name):
        with open(file_name, 'r') as f:
            for row in csv.reader(f):
                a, b, c = map(float, row)
                func(a, b, c)

    return wrapper


@find_quadratic_from_file
def solve_equation(a, b, c):
    descrim = b ** 2 - 4 * a * c
    if descrim < 0:
        print(None)
    elif descrim == 0:
        print(-b / (2 * a))
    elif descrim > 0:
        root1 = (-b - (descrim ** 0.5)) / (2 * a)
        root2 = (-b + (descrim ** 0.5)) / (2 * a)
        print(root1, root2)


print(solve_equation('save_file.csv'))
