# Grade calculator 

grade = input("Enter your numbers:")
grade = int(grade)

if 80 <= grade < 100:
    print("A")
elif 70 <= grade < 80:
    print("B")
elif 60 <= grade < 70:
    print("C")
elif 50 <= grade < 60:
    print("D")
elif grade > 100:
    print("Invalid number") 
else:
    print("FAIL")