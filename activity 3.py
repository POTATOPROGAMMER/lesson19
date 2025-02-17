try:
    num1,num2= eval(input("enter the two numbers seperated by a comma , : "))
    result = num1/num2
    print("result is  : " ,  result)
except ZeroDivisionError:
    print("cannot divide by zero ")
except SyntaxError:
    print("invalid syntax comma needed between two numbers")
except:
    print("an exception occured")
finally:
    print("finally block")