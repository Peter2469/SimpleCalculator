import math

print("Simple Calculator")
print("----------------------------")
fn = int(input("What is your first number "))
sn = int(input("What is your second number "))
print("----------------------------")
wat = input("""Please Select what you want to do
A = Addition
B = Subtraction
C = Times
D = Dividing
""")
print("----------------------------")
if wat == ("A"):
    print(fn , "+" , sn , "=" , fn + sn)

if wat == ("B"):
    print(fn , "-" , sn , "=" , fn - sn)

if wat == ("C"):
    print(fn , "*" , sn , "=" , fn * sn)

if wat == ("D"):
    print(fn , "/" , sn , "=" , fn / sn)


input("Press Enter")
