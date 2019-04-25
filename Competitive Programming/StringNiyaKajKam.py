n = int(input())

i = 0
while i < n:
    s1 = ""
    s2 = ""
    s = input()
    j = 0
    while j < len(s):
        if j % 2 == 0:
            s1 = s1 + s[j]
        else:
            s2 = s2 + s[j]
        j += 1
    i += 1
    print(s1,s2)
    #print(s2)

