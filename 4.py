import json
import csv


def save_json(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        data = {"args": args, "kwargs": kwargs, "result": result}
        with open("to_json.json", 'a') as f:
            json.dump(data, f)
            f.write('\n')
        return result

    return wrapper


def find_quadratic_from_file(func):
    def wrapper(file_name):
        with open(file_name, 'r') as f:
            for row in csv.reader(f):
                a, b, c = map(int, row)
                func(a, b, c)

    return wrapper


@find_quadratic_from_file
@save_json
def solve_equation(a, b, c):
    descrim = b ** 2 - 4 * a * c
    if descrim < 0:
        return None
    elif descrim == 0:
        return -b / (2 * a)
    elif descrim > 0:
        root1 = (-b - (descrim ** 0.5)) / (2 * a)
        root2 = (-b + (descrim ** 0.5)) / (2 * a)
        return root1, root2


print(solve_equation('save_file.csv'))
