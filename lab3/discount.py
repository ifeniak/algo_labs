import random


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
    random.shuffle(prices)
    ideal_pivot_idx = len(prices) - (len(prices) // 3) - 1
    pivot_idx = find_pivot(prices, ideal_pivot_idx, 0, len(prices) - 1)
    return "%.2f" % (sum(prices[:pivot_idx + 1]) + sum(prices[pivot_idx + 1:]) * (100 - discount) / 100)


def partition(prices, left, right):
    pivot = prices[right]
    i = left
    for j in range(left, right):
        if prices[j] < pivot:
            prices[j], prices[i] = prices[i], prices[j]
            i += 1
    prices[right], prices[i] = prices[i], prices[right]
    return i


def find_pivot(prices, ideal_pivot_idx, left, right):
    pivot_idx = partition(prices, left, right)
    if pivot_idx > ideal_pivot_idx:
        return find_pivot(prices, ideal_pivot_idx, left, pivot_idx - 1)
    elif pivot_idx < ideal_pivot_idx:
        return find_pivot(prices, ideal_pivot_idx, pivot_idx + 1, right)
    else:
        return pivot_idx


write_output()
