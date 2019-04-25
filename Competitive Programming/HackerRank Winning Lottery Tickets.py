############# T L E ################

def winningLotteryTicket(tickets):
    winPair = 0

    for i in range(0,len(tickets)-1):
        for j in range(i,len(tickets)):
            if isWinningPair(tickets[i],tickets[j]):
                winPair = winPair + 1
    return winPair

def isWinningPair(a,b):
    x = a + b
    #print(x)
    x = set(x)

    #print(x)
    #print(len(x))

    if len(x) == 10:
        return True
    else:
        return False


n = int(input().strip())
tickets = []
tickets_i = 0
for tickets_i in range(n):
   tickets_t = str(input().strip())
   tickets.append(tickets_t)
result = winningLotteryTicket(tickets)
print(result)