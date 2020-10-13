def sort(x):
    return abs(x)


def main():
    data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
    print('Исходные данные: ', data)
    result = sorted(data, key=sort, reverse=True)
    print('Сортировка без lambda-функции: ', result)

    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
    print('Сортировка при помощи lambda-функции: ', result_with_lambda)


if __name__ == "__main__":
    main()
