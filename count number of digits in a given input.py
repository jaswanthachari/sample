var = int(input('enter how many digits you want to enter (3 or 4): '))
if(var!=3 and var!=4):
    print("ONLY FOR 3 DIGIT NUMBER OR 4 DIGIT NUMBER ")
if(var==3):
    num = int(input("Enter the first digit of the number : "))
    num1 = int(input("Enter the second digit of the number : "))
    num2 = int(input("Enter the third digit of the number : "))
elif(var==4):
    num = int(input("Enter the first digit of the number : "))
    num1 = int(input("Enter the second digit of the number : "))
    num2 = int(input("Enter the third digit of the number : "))
    num3 = int(input("Enter the fourth digit of the number : "))


if(num == 1):
    print("One" , end=" ")
elif(num==2):
    print("Two", end=" ")
elif(num==3):
    print("Three", end=" ")
elif(num==4):
    print("Four", end=" ")
elif (num == 5):
    print("Five", end=" ")
elif (num == 6):
    print("Six", end=" ")
elif (num == 7):
    print("Seven", end=" ")
elif(num==8):
    print("Eight", end=" ")
elif(num==9):
    print("Nine", end=" ")



if(num1 == 1):
    print("One", end=" ")
elif(num1==2):
    print("Two", end=" ")
elif(num1==3):
    print("Three", end="  ")
elif(num1==4):
    print("Four", end=" ")
elif (num1== 5):
    print("Five", end=" ")
elif (num1== 6):
    print("Six", end=" ")
elif (num1== 7):
    print("Seven", end=" ")
elif(num1==8):
    print("Eight", end=" ")
elif(num1==9):
    print("Nine", end=" ")


if(num2== 1):
    print("One", end=" ")
elif(num2==2):
    print("Two", end=" ")
elif(num2==3):
    print("Three", end=" ")
elif(num2==4):
    print("Four", end=" ")
elif (num2== 5):
    print("Five", end=" ")
elif (num2== 6):
    print("Six", end=" ")
elif (num2== 7):
    print("Seven", end=" ")
elif(num2==8):
    print("Eight", end=" ")
elif(num2==9):
    print("Nine", end=" ")


if(num3== 1):
    print("One", end=" ")
elif(num3==2):
    print("Two", end=" ")
elif(num3==3):
    print("Three", end=" ")
elif(num3==4):
    print("Four", end=" ")
elif (num3== 5):
    print("Five", end=" ")
elif (num3== 6):
    print("Six", end=" ")
elif (num3== 7):
    print("Seven", end=" ")
elif(num3==8):
    print("Eight", end=" ")
elif(num3==9):
    print("Nine", end=" ")

str1=input("Enter anything here : ")
str2=len(str1)
for char in range(0,len(str1)) :
    if (str2%2==0) :
        print(str1[char].upper(),end='')
    else:
        print(str1[char].lower(), end='')


