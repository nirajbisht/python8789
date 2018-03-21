student_marks={'harry':1,'berry':2,'tina':3,'akriti':4,'harsh':5}
query_name=input("enter name=")
for item in student_marks:
	if item==query_name:	
		print(student_marks.get(item))