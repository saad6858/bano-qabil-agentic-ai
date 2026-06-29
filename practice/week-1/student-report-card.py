# This program is used to make a student report card

name=input("Enter your Name: ")

sub_1=int(input("enter you marks (out of 100) in subject 1: "))
sub_2=int(input("enter you marks (out of 100) in subject 2: "))
sub_3=int(input("enter you marks (out of 100) in subject 3: "))

total=sub_1+sub_2+sub_3
per= (total/300)*100
if(per>=90):
	grade="A"
elif(per>=80):
	grade="B"
elif(per>=70):
	grade="C"
elif(per>=60):
	grade="D"
elif(per<60):
	grade="F"
print("")
print("			REPORT CARD			")
print("Name:",name)
print("Total:",total,"/300")
print("Percentage: ",per)
print("Grade:",grade)