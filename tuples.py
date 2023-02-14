class Tuple():
    """Tuples are ordered, unchangeable and allows duplicates"""
    tuple1 = ('mac', 'laptop', 'mobile')
    tuple2 = ('java', 'python', 'selenium')

    def __int__(self, tuple1, tuple2):
        self.tuple1 = tuple1
        self.tuple2 = tuple2

    def tuple_methods(self):
        # Add tuples
        print("After adding the tuples:", self.tuple2 + self.tuple1)
        # Add values to tuple, as there are unchangable we cannot add , but we can convert to list add the elemnts
        # and again convert back to tuple

        modify = list(self.tuple1)
        modify.insert(3, 'desktop')
        self.tuple1 = tuple(modify)
        print("After modifying:", self.tuple1)

        # get count, tuple methods are index(), count()
        print(self.tuple1.count('desktop'))
        print(self.tuple1.index('desktop'))

        # unpack tuples
        (m, *l, d) = self.tuple1
        print(m, l, d)


tuple_examples = Tuple()
tuple_examples.tuple_methods()
