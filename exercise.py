class Error(Exception):
    pass

class PWTooSmallError(Error):
    pass

class PWTooLargeError(Error):
    pass

while True:
    try:
        i_num = int(input("Enter a password: "))
        if i_num<6 :
            raise PWTooSmallError
        elif i_num>20:
            raise PWTooLargeError
        break
    except PWTooSmallError:
        print("This pw too small, try again")
    except PWTooLargeError:
        print("this pw too large, try again")
print("congrats, you're pretty good")