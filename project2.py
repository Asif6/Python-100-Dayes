print("Welcome to the tip calculator!")

Total_Bill=float(input("What was the total bill? $"))
Tip_percentage =float(input("How mch tip would you like to give? 10, 12, or 15?"))
Number_of_people=int(input("How many people to split the bill?"))
Tip=Total_Bill* Tip_percentage/100
Total_Bill_With_Tip=Total_Bill+Tip

Each_Person_Bill=Total_Bill_With_Tip/Number_of_people

final_amount= "{:.2f}".format(Each_Person_Bill)

print(f"Each person should pay ${final_amount}")

