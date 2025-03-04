# 0 1 1 2 3 5 8
def fibonacii(n):
    num1=0
    num2=1
    nextnum = num2
    for i in range(n):
        num1 = num2
        num2 = nextnum
        nextnum = num1 + num2
        print(nextnum)

def fibonaciifactorial(n):
    if n<0:
        print("wrong input")
    elif n ==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return (fibonaciifactorial(n-1) + fibonaciifactorial(n-2))

for i in range(5):
    print(fibonaciifactorial(i))

# 4

# f(3) + f(2)

# fib(3)
# f(2) + f(1) = 2

# 2+1 =3