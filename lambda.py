
def myfunc(a):
    x = lambda a, b, c: a + b + c
    print(x(a, 20, 30))

    name = 'anvika'
    reverse = lambda string:string[::-1]
    print(reverse(name))


myfunc(3)

def max(a,b):
    greater = lambda a,b : a if(a>b) else b
    print(greater(a,b))

max(10,20)


sequences = [3, 5, 7, 9]
new_list = map(lambda num :num*num, sequences)
print(list(new_list))

new_list = filter(lambda num: num>6, sequences)
print(list(new_list))










