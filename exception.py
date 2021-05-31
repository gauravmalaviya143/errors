a = 5
b = 2

try:
    print("resource open")
    print(a/b)
    k = int(input("enter the number"))
    print(k)

except ZeroDivisionError as e:
    print("You cannot divide number by zero")

except ValueError as e:
    print("Invalid input")

except Exception as e:
    print("something went wrong")

finally:
    print("resource closed")