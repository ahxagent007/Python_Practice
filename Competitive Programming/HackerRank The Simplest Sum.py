## BAKI ASE CODING AKHONO #######

import sys

def simplestSum(k, a, b):
    sumS = 0
    for i in range(a,b+1):
        sumS += fuck(k, i)

    return sumS

def fuck(k, n):
    sumX = 0
    #(sum, "for ", k, " ", n)

    i = 1
    while (i <= n):
        sumX += i
        print(i, "*", k, " = ")
        i *= k
        print(i)
        print(i, " <= ", n)

    print(sumX, "for ", k, " ", n)
    return sumX


if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        k, a, b = input().strip().split(' ')
        k, a, b = [int(k), int(a), int(b)]
        result = simplestSum(k, a, b)
        print(result)
