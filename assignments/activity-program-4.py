# This program takes marks in percentage from the user and print his grade

per = float(input("Enter your marks in percentage: "))
if(per>90):
	print("A")
elif(per>80):
	print("B")
elif(per>70):
	print("C")
elif(per>60):
	print("D")
elif(per>50):
	print("E")
else:
	print("F")