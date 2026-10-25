class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self._iterator = iter(items)
        self._seen = set()

    def __next__(self):
        while True:
            item = next(self._iterator)

            if self.ignore_case and isinstance(item, str):
                key = item.lower()
            else:
                key = item

            if key not in self._seen:
                self._seen.add(key)
                return item

    def __iter__(self):
        return self


if __name__ == '__main__':
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print(list(Unique(data)))

    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(list(Unique(data)))
    print(list(Unique(data, ignore_case=True)))

    def gen():
        yield from [1, 1, 2, 2, 3, 3]

    print(list(Unique(gen())))