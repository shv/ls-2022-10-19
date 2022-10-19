# class IterMainClass:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#
#     def __iter__(self):
#         return IterClass(self.start, self.stop)
#
#
class IterClass:
    def __init__(self, start, stop):
        self.start = start - 1
        self.stop = stop

    def __iter__(self):
        value = self.start
        while value < self.stop:
            value += 1
            yield value ** 2


r = IterClass(1, 5)

i1 = iter(r)
i2 = iter(r)


print(next(i1))
print(next(i1))
print(next(i2))
print(next(i2))

# print([i for i in r])
# print([i for i in r])
# print([i for i in r])

# i1 = iter(r)
# i2 = iter(r)
#
# print(next(i1))
# print(next(i1))
# print(next(i1))
# print(next(i2))
# print(next(i2))
