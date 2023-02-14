# parameterized function
def calculate(a, b):
    total = a + b
    print(total)


calculate(10, 20)  # parameterized function


# un parameterized
def calculate():
    total = 10 + 20
    print(total)


calculate()


def arguments(*args):
    print("number :", args[2])


arguments('2', '3', '3')

#key value pair
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="ram", child2="hari", child3="sindhu")


# if number of keyword arguments are un known pass **
def keyWord(**values):
    print("name :", values['lname'])


keyWord(fname='anvika', lname='yendela', zip='503001')
