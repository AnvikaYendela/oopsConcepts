class Lists:
    """Lists is collection where items are ordered,changeable,allows duplicates """

    list1 = ['a', 'b', 'c', 'd']
    list2 = ['e', 'f', 'f', 'g']

    def __int__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def change_values(self):
        self.list1[1] = 'ball'
        self.list2[0] = 'elephant'
        print(self.list1)
        print(self.list2)

        print("Print list with mentioned range:", self.list1[0:2])
        print("Print list with mentioned range:", self.list1[0:])
        print("Print list with mentioned range:", self.list1[-2:])

        self.list1[0:2] = ['apple', 'banana']

        print("Print values which is to be replaced with specific range", self.list1)

        self.list1[0:4] = ['animal', 'box']

        print("Print values which is to be replaced with specific range", self.list1)

        self.list1.append('cat')
        print("Append values to list:", self.list1)

        self.list1.insert(3, 'dog')
        print("Add values to a specific position", self.list1)

        # del, pop, clear()
        # clear() will empty the list
        # pop() - if you dont specify index it will remove the last item
        self.list1.remove('dog')
        print("Remove value", self.list1)

    def looping(self):
        new_list = []
        for index in self.list2:
            if "e" in index:
                new_list.append(index)
        print(new_list)

        i = 0
        while i < len(self.list1):
            print(self.list1[i])
            i = i + 1

        # list comprehension - minimise the syntax, short hand representation
        new_list = [index for index in self.list2 if "e" in index]
        print(new_list)



lists = Lists()
lists.change_values()
lists.looping()
