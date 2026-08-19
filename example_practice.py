#calculate_stats.py
print("--- Grade statistics ---")

# Get grades as input
grade1 = float(input("enter grade 1: "))
grade2 = float(input("enter grade 2: "))
grade3 = float(input("enter grade 3: "))

# Put grades into a list for sum/min/max functions
grades = [grade1 , grade2, grade3]

# calculate sum and average 
total_grades = sum(grades)
num_grades = len(grades) # len() works for strings and lists!
average_grade = total_grades / num_grades
# find highest and lowest
highest_grade = max(grades)
lowest_grade = min(grades)

# Round the average for display
rounded_average = round(average_grade,2)

print("\n--- results ---")
print("entered grades:", grades)
print("Total points:", total_grades)
print("Average grade:", rounded_average)
print("Highest grade:", highest_grade)
print("Lowest grade:", lowest_grade)