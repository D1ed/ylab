class CyclicIterable:
    def __init__(self, data):
        self._data = list(data)

    def __iter__(self):
        while True:
            yield from self._data

cycle = CyclicIterable(range(3))
for i in cycle:
    print(i)