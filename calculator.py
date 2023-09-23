

def calculator(operator, num1, num2):
    if operator == 1:
        print( num1 * num2)
    if operator == 2 and (num1 and num2 != 0): 
        print(num1 / num2)
    if operator == 3:
        print( num1 + num2)
    if operator == 4:
        print (num1 - num2)


print('These are the operators:\n ')
print(' 1-Click 1 for the multiplication\n 2-Click 2 for the division\n 3-Click 3 for addition\n 4-Click 4 for substraction \n')

operator = int(input())

while operator not in [1,2,3,4]:
    print('Invalid operator...... Try again')
    operator = int(input())

print('Choose the first number: ')   
user_input = float(input())

print('Choose the second number: ')
user_input2 = float(input())

if (operator == 2 and user_input2 == 0):
        print("Sorry you can't divide by 0")

calculator(operator, user_input, user_input2)
    


         
