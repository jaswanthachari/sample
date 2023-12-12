l = []
maximum = int(input("Enter the number of elements you want to add in a list : "))
for i in range (0,maximum):
    n = int(input())
    l.append(n)

num = int(input("Enter the number you want to search in the list : "))
position = -1
for i in range(0,len(l)):
    if l[i]==num :
        position=i+1
    if position == -1 :
        print(f"Number {num} is not present in the list.")
        break
    else:
        print(f"Number {num} is present at {position+1} position : ")
        break