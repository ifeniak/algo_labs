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
    real_discount = (100 - discount) / 100
    distribution = create_counting(prices)
    low_num = len(prices) - (len(prices) // 3)
    i = 0
    while distribution[i] < low_num:
        i += 1
    pivot = distribution.index(distribution[i]) + min(prices)
    result = pivot * (distribution[i] - low_num) * real_discount
    if i != 0:
        result += pivot * (low_num - distribution[i - 1])
    else:
        result += pivot * low_num
    result += sum(price for price in prices if price < pivot)
    result += sum(price * real_discount for price in prices if price > pivot)
    return "%.2f" % result


def create_counting(prices: list):
    high_bound = max(prices)
    low_bound = min(prices)
    distribution = [0] * (high_bound - low_bound + 1)
    for price in prices:
        distribution[price - low_bound] += 1
    for i in range(1, len(distribution)):
        distribution[i] += distribution[i - 1]
    return distribution

print(best_purchase([1, 1, 1], 33))
write_output()
