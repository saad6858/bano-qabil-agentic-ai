inport display
while True:
	name=input("Enter student name: ")
	marks=int(input("Enter your marks in percentage: "))
	display.display_result(name,marks)
	choice=input("Is there any other student? (yes/no): ")
	if(choice.lower() != "yes"):
		break