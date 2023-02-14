class Sets:
    """Sets is a collection which is unordered , unchangeable, and allows un indexed , do not allow duplicate values"""

    set1 = {'twitter', 'linkedin', 'facebook'}

    def __int__(self, set1):
        self.set1 = set1

    def sets_methods(self):
        for x in self.set1:
            print(x)
        set2 = {'whatsapp','chat'}
        self.set1.update(set2)
        print(self.set1)

        set2.add('abcdef')
        print(set2)

        self.set1.union(set2)
        print(self.set1)

        



sets = Sets()
sets.sets_methods()