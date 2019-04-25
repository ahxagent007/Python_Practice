a = int(input())

if a%10 > 5:
    a = a + (10-a%10)
else:
    a = a - a%10

print(a)