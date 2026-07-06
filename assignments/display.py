import grade
def display_result(name,marks):
	grade_ = grade.calculate_grade(marks)
	print("---- Student Result ----")
	print("Name:",name)
	print("Marks:",marks)
	print("grade:",grade_)