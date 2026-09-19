print("Student Grade Calculator")

marks = []

for i in range(1, 6):
    while True:
        try:
            mark = float(input(f"Enter marks for Subject {i}: "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

total = sum(marks)
percentage = total / 5

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"

if percentage >= 40:
    status = "PASS"
else:
    status = "FAIL"

print("\n----- Result Summary -----")
print("Total Marks:", total)
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
print("Status:", status)