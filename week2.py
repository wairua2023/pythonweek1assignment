# simple bill calculator
price = float(input("Enter price of one item: "))
quantity = int(input("Enter the quantity: "))
total = price * quantity

print(f"{quantity} items at {price:.2f} total {total:.2f}")