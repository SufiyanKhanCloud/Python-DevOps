user_name = input("Enter your name:")
age =  input("Enter your age:")

age = int(age)

if age >= 18:
    print("an Adult")
else:
    print("a Minor")

print("User name is {} and he is {}".format(user_name, age))