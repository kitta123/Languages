def divide(x, y):
    try:
        result = x // y
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError as error:
        print("Sorry ! You are dividing by zero ")
    except Exception as error:
        print("Exception error")

x = int(input("enter the number :"))
y = int(input("enter the number :"))
divide(x,y)
