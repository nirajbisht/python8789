string=input("enter string=")
sub_string=input("enter string to find=")
count=0
for c,i in enumerate(string):
    if i == sub_string[0]:
        if string[c:c+len(sub_string)] == sub_string:  
            count+=1
return count