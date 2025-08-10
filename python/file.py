import os 

print(os.listdir("."))

if os.path.exists("file.txt"):
    print("File exists")
else:
    print("File does not exist")

with open("file.txt", "r") as file:
    content = file.read()

with open("output.txt", "w") as file:
    file.write("Hello, file!")    