sp = int (input("Enter the selling price of the product ; "))
cp = int (input("Enter the cost price of the product ; "))
if sp>cp:
    p = sp-cp
    print(f"You have got RS{p} profit. ")
elif cp>sp:
    l = cp-sp
    print(f"You have got RS{l} loss. ")
elif cp==sp:
    print("No profit No loss")