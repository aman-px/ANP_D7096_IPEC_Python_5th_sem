# n program to accept the purchase amount and display whether the parking fee is 
# waived or payable. 
purchase_amount = float(input("Enter the Purchase amount : "))

# to validate amount 
if(purchase_amount < 0):
    exit("Amount should be positive  ")
# to verify the purchase amount 
if(purchase_amount >= 2000):
    print("Mall Waives the parking fee ")

else:
    print("you must have to pay parking fee of 100 rs.")  