number_int = int(input("Enter some numbers, input ends if it is 0: "))
count_int = 0
total_int = 0
positive_int = 0
negative_int = 0
sentinel = 0
while number_int != sentinel:
    int(input("Enter some numbers, input ends if it is 0: "))
    total_int = total_int + count_int
    if number_int > 0:
        positive_int += 1
    else:
        negative_int += 1
    count_int += 1

average_float = total_int / count_int

print("Average is:", average_float)
print("Total is:", total_int)
