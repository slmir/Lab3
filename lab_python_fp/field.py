def field(items, *args):
    assert len(args) > 0
    #Вывод значений одного ключа
    if len(args) == 1:
        for d in items:
            if args[0] in d.keys() and not d[args[0]] is None:
                yield d[args[0]]
    else:
        for d in items:
            elem = {}
            for arg in args:
                if arg in d.keys() and not d[arg] is None:
                    elem[arg] = d[arg]
            if len(elem) != 0:
                yield elem


def main():
    paintings = [
        {'title': 'Мадонна', 'price': 2000, 'year': '1951'},
        {'title': 'Бурлаки на Волге', 'year': '1820'},
        {'title': 'Мишки в сосновом бору', 'price': 5000},
        {'title': 'Шторм', 'price': 35000, 'year': '1859'},
        {'title': '9-ый вал', 'year': '1910'}
    ]

    print("Пример генератора, который последовательно выдает значения ключей словаря")
    print("\nВывод только названий по ключу title:\n", str(list(field(paintings, 'title'))))
    print("\nВывод названий и цены :\n", str(list(field(paintings, 'title', 'price'))))
    print("\nВывод названий,цены и года написания:\n", str(list(field(paintings, 'title', 'price', 'year'))))

if __name__ == "__main__":
    main()



