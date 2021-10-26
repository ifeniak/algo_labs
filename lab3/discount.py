import collections


def read_input():
    f = open("discnt.in", "rt")
    prices_string = f.readline()
    prices = [int(word) for word in prices_string.split() if word.isdigit()]
    discount = int(f.readline())
    f.close()
    return prices, discount


def write_output():
    f = open("discnt.out", "w")
    result = best_purchase(*read_input())
    f.write(str(result))
    f.close()


def best_purchase(prices: list, discount):
    prices.sort()
    prices = collections.deque(prices)
    min_sum = 0
    for _ in range(len(prices) // 3):
        min_sum += prices.popleft()
        min_sum += prices.popleft()
        min_sum += prices.pop() * (100 - discount) / 100
    if prices is not None:
        min_sum += sum(prices)
    return "%.2f" % min_sum


write_output()
