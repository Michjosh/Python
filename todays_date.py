todays_date = int(input("Enter today's day"))

if todays_date == 0:
    print("Sunday")
if todays_date == 1:
    print("Monday")
if todays_date == 2:
    print("Tuesday")
if todays_date == 3:
    print("Wednesday")
if todays_date == 4:
    print("Thursday")
if todays_date == 5:
    print("Friday")
if todays_date == 6:
    print("Saturday")

elapsed_days = int(input("Enter the number of days elapsed since today"))
future = todays_date + elapsed_days % 7

if future == 0:
    print("future is Sunday")
elif future == 1:
    print("future is Monday")
elif future == 2:
    print("future is Tuesday")
elif future == 3:
    print("future is Wednesday")
elif future == 4:
    print("future is Thursday")
elif future == 5:
    print("future is Friday")
elif future == 6:
    print("future is Saturday")

