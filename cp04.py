def calculator(num1,num2):
    print('Choose the operator')
    operator = input()
    if operator == '*':
        print( num1 * num2)
    if operator == '/':
        print(num1 / num2)
    if operator == '+':
        print( num1 + num2)
    if operator == '-':
        print (num1 - num2)
  
user_input = int(input())
user_input2 = int(input())
if user_input and user_input2 == 0:
    exit()
 

calculator(user_input,user_input2)
