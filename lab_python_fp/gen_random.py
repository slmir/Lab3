import random


def gen_random(num_count, begin, end):
    string1 = ""
    #get_rand = [random.randint(begin, end) for i in range(num_count)]
    #print(get_rand)
    for i in range(num_count):
        yield random.randint(begin, end)
        #if i == num_count-1:
        #    string1 += "{}".format(random.randint(begin, end))
        #    break
        #string1 += "{}, ".format(random.randint(begin, end))
    #print(string1)

def main():
    print("Пример генератора 10 случайных чисел от -10 до 10")
    print(str(list(gen_random(10, -10, 10)))[1:-1])

if __name__ == "__main__":
    main()

