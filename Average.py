# 10 Python program to find the average of 10 numbers using while loop
count = 0
my_sum = 0.0
while count < 10:
    number = float(input("Enter a real number: "))
    count = count + 1
    my_sum = my_sum + number
avg = my_sum / 10
print("Average is :", avg)
