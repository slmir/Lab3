def print_result(func):
    def wrapper(*args):
        print(func.__name__)
        return_value = func(*args)
        if isinstance(return_value,list):
            print('\n'.join(str(value) for value in return_value))
        elif isinstance(return_value,dict):
            print('\n'.join((str(key) + ' = ' + str(return_value[key]) for key in return_value.keys())))
        else:
            print(return_value)
        return return_value
    return wrapper



@print_result
def test_1():
    return 1

@print_result
def test_2():
    return 'iu'

@print_result
def test_3():
    return {'a': 1, 'b': 2}

@print_result
def test_4():
    return [1, 3]

def main():
    print("\nПример реализации декоратора")

    test_1()
    test_2()
    test_3()
    test_4()

if __name__ == "__main__":
    main()