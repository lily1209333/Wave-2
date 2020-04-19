month = str(input("Enter a month (with the first letter capatlized): "))
odd = ["January", "March", "May", "July", "August", "October", "December"]
even = ["April", "June", "September", "November"]
if month in odd:
    print("31 days")
elif month in even:
    print("30 days")
elif month == "February":
    print("28 or 29 days")
