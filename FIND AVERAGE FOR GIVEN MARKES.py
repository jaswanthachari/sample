n = int(input("Enter how many marks you want to enter ; "))
l =[]
for i in range (0,n):
    a = int (input("Enter mark: "))
    l.append(a)


s = sum(l)
average = s/ n
print(average)
