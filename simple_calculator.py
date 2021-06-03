#simple calculator
num1=int(input('Enter the first number: '))
num2=int(input('Enter the second number: '))
print('1. Addition')
print('2.Subtraction')
print('3. Multiplication')
print('4. Division')
choice=0
for choice in range (4):
    choice=int(input('Please enter you choice:  '))
    if choice==1:
        print('The sum is :', num1+num2)
    elif choice==2:
        print('The difference is: ', num1-num2)
    elif choice==3:
        print('The product is: ', num1*num2)
    elif choice==4:
        print('The quotient is: ', num1//num2, 'and the remainder is ', int(num1 % num2))
    else:
        print('Invalid choice')