from lab_python_fp.gen_random import gen_random


class Unique(object):
    def __init__(self,items,**kwargs):
        self.data = []
        strings = []
        for i in items:
            if isinstance(i, str):
                if 'ignore_case' in kwargs.keys() and kwargs['ignore_case'] is True:
                    if i.lower() not in strings:
                        strings.append(i.lower())
                        self.data.append(i)
                else:
                    if i not in self.data:
                        self.data.append(i)
            else:
                if i not in self.data:
                    self.data.append(i)


    def __next__(self):
        if not self.data:
            raise StopIteration
        return self.data.pop(0)

    def __iter__(self):
        return self


def main():
    data1 = [1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 2, 1]
    data2 = gen_random(5, 0, 2)
    data3 = ['a', 'b', 'c', 'A', 'B', 'C']

    print("Пример итератора уникальных данных")
    print(str(list(Unique(data1))))
    print(str(list(Unique(data2))))
    print(str(list(Unique(data3))))
    print(str(list(Unique(data3, ignore_case=True))))  # без учета регистра

if __name__ == "__main__":
    main()

