# 5 Python program to implement linear search

numbers = [4, 2, 7, 1, 8, 3, 6]
# flag
f = 0
x = int(input("Enter the number find: "))
for i in range(len(numbers)):
    if x == numbers[i]:
        print(" Successful search, the element is found at position", i)
        f = 1
        break
if f == 0:
    print("Unsuccessful")
