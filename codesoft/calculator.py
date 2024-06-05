def add(X, Y):
    return X + Y
def subtract(X, Y):
    return X - Y
def multiply(X, Y):
    return X * Y
def divide(X, Y):
    return X / Y

print("Please select the operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Please enter choice (1/ 2/ 3/ 4): ")

num_1 = int(input("Please enter the first number: "))
num_2 = int(input("Please enter the second number: "))

if choice == '1':
    print(num_1, " + ", num_2, " = ", add(num_1, num_2))

elif choice == '2':
    print(num_1, " - ", num_2, " = ", subtract(num_1, num_2))

elif choice == '3':
    print(num_1, " * ", num_2, " = ", multiply(num_1, num_2))

elif choice == '4':
    print(num_1, " / ", num_2, " = ", divide(num_1, num_2))
else:
    print("This is an invalid input")