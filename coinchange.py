import time

def coinChange(coins, amount):
    m = 2**31 - 1

    def coinChangeHelper(index, amount, count):
        nonlocal m, coins

        if amount == 0:
            m = min(m, count)

        for j in range(index, len(coins), 1):
            if coins[j] <= amount < (m - count)*coins[j]: # most important line
                n = amount//coins[j]
                i = n
                while i > 0:
                    if amount - i * coins[j] < (m - count - i)*coins[j]: # most important line
                        coinChangeHelper(j+1, amount - i*coins[j], count + i)
                    else:
                        break
                    i -= 1


    coins.sort(reverse = True)
    coinChangeHelper(0, amount, 0)
    return m if m < 2**31 - 1 else -1


t0 = time.time()
print(coinChange([243,291,335,209,177,345,114,91,313,331], 1000000000))
#print(coinChange([88,227,216,96,209,172,259], 6928))
#print(coinChange([5,306,188,467,494], 7047))
#print(coinChange([1, 2, 5], 11))
#print(coinChange([3, 10, 25], 51))
#print(coinChange([186, 419, 83, 408], 6249))
print(time.time() - t0)
