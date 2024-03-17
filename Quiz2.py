def even(e):
    even_list.append(e)
def odd(o):
    odd_list.append(o)


def list(L):
    global even_list
    even_list=[]
    global odd_list
    odd_list = []
    for i in L:
        if (i%2==0):
            even(i)
        else:
            odd(i)
    print("The list of odd numbers are:",odd_list)
    print("The list of even numbers are:",even_list)

L=[12, 15, 33, 7, 1, 92, 53, 4,0]
print("The list is ")
print(L)
list(L)