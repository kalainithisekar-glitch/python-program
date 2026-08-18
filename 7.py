mark = int(input("Enter your mark: "))

if mark >= 90 and mark <= 100:
    print("Grade S")
elif mark >= 80 and mark <= 89:
    print("Grade A")
elif mark >= 70 and mark <= 79:
    print("Grade B")
elif mark >= 60 and mark <= 69:
    print("Grade C")
elif mark >= 40 and mark <= 59:
    print("Grade D")
else:
    print("Fail")
