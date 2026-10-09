# url="http://127.0.0.1:5501/index.html"
def SelectSupplies(items, W):
    n = len(items)
    dp = [[0 for c in range(W + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        weight = items[i - 1][1]
        value = items[i - 1][2]
        for c in range(W + 1):
            dp[i][c] = dp[i - 1][c]
            if weight <= c:
                dp[i][c] = max(
                    dp[i][c],
                    dp[i - 1][c - weight] + value
                )
    chosen = []
    c = W
    for i in range(n, 0, -1):
        if dp[i][c] != dp[i - 1][c]:
            chosen.append(items[i - 1])
            c -= items[i - 1][1]
    chosen.reverse()
    return dp[n][W], chosen
n = int(input("Enter number of supplies: "))
items = []
for i in range(n):
    name = input("Enter supply name: ")
    weight = int(input("Enter weight: "))
    value = int(input("Enter usefulness value: "))
    items.append((name, weight, value))
W = int(input("Enter vehicle capacity: "))
max_value, chosen = SelectSupplies(items, W)
print("\nSelected Emergency Supplies:")
total_weight = 0
for item in chosen:
    print(item[0], "- Weight:", item[1],
          "kg, Usefulness:", item[2])
    total_weight += item[1]
print("Total Weight:", total_weight, "kg")
print("Maximum Usefulness:", max_value)