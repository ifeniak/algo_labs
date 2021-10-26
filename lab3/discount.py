import collections


def best_purchase(prices: list, discount):
    prices.sort()
    prices = collections.deque(prices)
    min_sum = 0
    for _ in range(len(prices) // 3):
        min_sum += max(0, prices.popleft())
        min_sum += prices.popleft()
        min_sum += prices.pop() * (100 - discount) / 100
    if prices is not None:
        min_sum += sum(prices)
    return min_sum



