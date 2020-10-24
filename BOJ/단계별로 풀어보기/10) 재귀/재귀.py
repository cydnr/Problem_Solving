# 10872 팩토리얼
def fac(n):
    if n == 0 :
        return 1
    else:
        return n * fac(n-1)
N = int(input())
print(fac(N))

# 10870 피보나치 수 5
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

N = int(input())
print(fib(N))