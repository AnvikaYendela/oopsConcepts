class Dictionaries:
    """Ordered, changable does not allow duplicates"""
    p_details = {
        "name": 'anvika',
        'id': '2002',
        'company': 'atmecs'
    }

    a_details = {
        "street": 'yellammagutta',
        'pincode': '503001',
        'dist': 'nizamabad'
    }

    def __int__(self, p_details, a_details):
        self.p_details = p_details
        self.a_details = a_details

    def methods(self):
        for keys in self.p_details.keys():
            print(keys)
        for values in self.p_details.values():
            print(values)

        for items in self.p_details.items():
            print(items)

        self.p_details['age'] = 28
        print("after updating:", self.p_details)

        self.p_details.update({'location': 'hyderabad'})
        print(self.p_details)

        self.p_details.pop('location')
        print(self.p_details)

    # nested dictionary

    phone1 = {
        "name": "apple",
        "version": 1
    }
    phone2 = {
        "name": "Tobias",
        "year": 2007
    }

    nested = {
        "child1": phone1,
        "child2": phone2,
    }
    print(nested["child1"]["name"])


dict = Dictionaries()
dict.methods()
