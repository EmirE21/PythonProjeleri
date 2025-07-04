prices = input().split(",")
items = input().split(",")
budget_per_item = int(input())

affordable_items = []
cant_afford = 0
total_needed = 0
for i in range(len(prices)):
    prices[i] = int(prices[i])
    if budget_per_item >= prices[i]:
        affordable_items.append(items[i])
        total_needed += prices[i]
    else:
        cant_afford = len(items)-len(affordable_items)

print("Can buy:", affordable_items)
print("Total budget needed:", total_needed)
print("Can't afford:", cant_afford)