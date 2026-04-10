amount = int(input("Enter the total purchase amount:"))
if amount >= 5000:
    discount = 0.20
elif amount >= 3000:
    discount = 0.10
else:
    discount = 0.00
final_bill = amount - (amount * discount)
print(f"Discount applied: {discount*100}%")
print(f"Final bill amount: {final_bill:.2f}")
