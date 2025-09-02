prices = [25, 15, 32, 8, 45, 13, 67, 23]
prices20 = []
for i in range(len(prices)):
    if prices[i] > 20:
        prices20.append(prices[i])
print(f"Sum: {sum(prices)}")
print("Price more than 20 is", prices20)