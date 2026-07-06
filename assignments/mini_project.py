# Function which calculates the grade of a student on the basis of marks in percentage
def calculate_grade(marks):
	if marks>100: return"Enter a valid percentage of marks i.e <=100"
	elif marks>=90: return"A+"
	elif marks>=80: return"A"
	elif marks>=70: return"B"
	elif marks>=60: return"C"
	elif marks>=50: return"D"
	else: return "Fail"

# Function which display the Student Result
def display_result(name,marks):
	grade = calculate_grade(marks)
	print("---- Student Result ----")
	print("Name:",name)
	print("Marks:",marks)
	print("grade:",grade)

# main part of the program which takes input and do all the work by calling other functions
while True:
	name=input("Enter student name: ")
	marks=float(input("Enter your marks in percentage: "))
	display_result(name,marks)
	choice=input("Is there any other student? (yes/no): ")
	if(choice.lower() != "yes"):
		break