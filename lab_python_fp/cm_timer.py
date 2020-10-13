import time
from time import sleep
from lab_python_fp.ptint_result import print_result


class cm_timer_1:
    def __enter__(self):
        self.time = time.clock()
        return self.time

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('time: ', time.clock() - self.time)


@print_result
def cm_timer_2():
    begin_time = time.time()
    yield 1
    print('time: ', time.time() - begin_time)


def main():
    print("Пример реализации контекстных менеджеров вывода времени работы блока кода")
    with cm_timer_1():
        time.sleep(3.5)

    with cm_timer_2():
        time.sleep(4.5)

if __name__ == "__main__":
    main()