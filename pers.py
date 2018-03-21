n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input("enter name=").split()
    scores = list(map(float, line))
    z=sum(scores)
    c = z/3
    student_marks[name] =c
query_name=input()
for key in student_marks:
    if key==query_name:
        print(student_marks.get(key))