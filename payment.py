print("Welcome to the payment calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10%, 12%, or 15% of the bill? "))
people = int(input("How many people to split the bill?"))
tip_per=bill*tip/100
each=(bill+tip_per)/people
print("Each person should pay: " + "%.2f"%each)
