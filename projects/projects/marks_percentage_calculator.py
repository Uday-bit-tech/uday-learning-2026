def calculate_percentage(total_marks, obtained_marks):
    percentage = (obtained_marks / total_marks) * 100
    return percentage

total = int(input("Enter Total Marks: "))
obtained = int(input("Enter Obtained Marks: "))

result = calculate_percentage(total, obtained)

print("Percentage =", round(result, 2), "%")
