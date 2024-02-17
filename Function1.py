""" Lenth ber korar jonno use korte hoy
Num1 = ["Hi","hello","Good","Day","For"]
Num2 = ["Best","Better","Last","Next"]

def Lenth(Hi):
    print(len(Hi))

Lenth(Num1)
Lenth(Num2)

"""
"""
# Using Loop print all Item

Num1 = ["Hi","hello","Good","Day","For"]
Num2 = ["Best","Better","Last","Next"]

def Lenth(Hi):
    print(len(Hi))

def Len(Hi):
    for item in Hi:
        print(item, end="")

print(Num1)

"""
"""
Name = ["Hi","Hello","good"]

def print_Len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item,end = " ")

print_list(Name)

"""
"""

# Factorial 

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
cal_fact(5)
"""
"""
# Usd to Bdt

def converter(Usd):
    BDT = Usd * 110
    print(Usd," USD =", BDT, "BDT")

converter(2)
"""

def evenodd(n):
    if n %2 == 0:
        print("Even")
    else:
        print("Odd")
evenodd(6)



