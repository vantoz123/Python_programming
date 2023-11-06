price = 1000000
credit = 0


is_good = False
if is_good == True:
    credit = price *(10/100)
    payable = price - credit
else:
    credit = price *(20/100)
    payable = price - credit

print(f"Since the buyer has a good credit the house will be {price} - {credit} = {payable}")
