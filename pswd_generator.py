import random

try:
    len = int(input('enter the length of password:'))

    lower_case = []
    for x in range(ord('a'),ord('z')+1):
      lower_case.append(chr(x))
    small_alpha = "".join(lower_case)
    

    upper_case = []
    for x in range(ord('A'),ord('Z')+1):
     upper_case.append(chr(x))
    upper_alpha = "".join(upper_case)
    

    num = []
    for x in range(10):
     num.append(str(x))
    digits = "".join(num)
    

    special_chars = '!@#$%^&*_-?|+='
    
    expression = small_alpha + upper_alpha + digits + special_chars

    if len >= 8:
            temp1 = random.sample(small_alpha ,1)
            temp2 = random.sample(upper_alpha ,1)
            temp3 = random.sample(digits ,1)
            temp4 = random.sample(special_chars ,1)
            temp5 = random.sample(expression, len-4)
            temp = temp1+temp2+temp3+temp4+temp5

            for i in temp:
                psswd = "".join(temp)
            print(psswd)

    elif len<8 or len == None:
            print("password must be atleast 8 characters long")

except SyntaxError as err:
    print('invalid input')

except NameError as e:
    print('length must be an integer')
except ValueError as e:
    print('length must be an integer')