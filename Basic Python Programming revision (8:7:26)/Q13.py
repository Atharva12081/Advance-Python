try :
    a = int(input())
    b = int(input())
    ans = a/b
except ZeroDivisionError:
    print("You Can not divide by zero")