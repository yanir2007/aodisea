num1 = int(input("length of the first side in a triangle: "))
num2 = int(input("the length of the second side in a triangle: "))
num3 = int(input("Type the length of the third side in a triangle: "))
if ((num1 + num2)>num3) and ((num1 + num3)>num2) and ((num2 + num3)>num1):
    print("It can be a triangle")
else:
    print("It can not be a triangle")