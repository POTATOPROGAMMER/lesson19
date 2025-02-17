try:
    age=int(input("enter age:" ,  ))
    if age<18:
      raise ValueError("age should be greater than 18")
    else:
       print("you are eliible")
except ValueError as e:
   print(e)
finally:
   print("finally block")

