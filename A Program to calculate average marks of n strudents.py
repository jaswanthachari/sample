l = []
n = int(input("Enter the number of students you want to enter : "))
for i in range (0,n):
    marks = int(input(f"Enter marks of student{i+1}: "))
    l.append(marks)
    total = 0
    for marks in l :
        total = total + marks
average = total/n
print(f"Average marks of {n} students are is : {average}")