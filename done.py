import os.path
import hashlib

class Error(Exception):
    pass

class PWTooSmallError(Error):
    pass

class PWTooLargeError(Error):
    pass

class AccountTooSmallError(Error):
    pass

class AccountTooLargeError(Error):
    pass

class FileAlreadyExists(Error):
    pass

address = os.getcwd()
count=0


while True:     
    name = input("filename: ")   
    if name != '--end-input--':
        try:              
            if  os.path.isfile(f"{name}.txt"):
                raise FileAlreadyExists             
            else:
                print("File not existed, creating file...\n")
                file = open(f"{address}\\{name}.txt", 'w')
                pass               
        except FileAlreadyExists:
            print("File already exists, please try again")
            continue
        while True:        
                account=input("account name: ")
                if account != '--end-input--':
                    try:
                        file = open(f"{address}\\{name}.txt", 'a+') 
                        pw = input("password: ")   
                        print()         
                        if len(account)>12:
                            raise AccountTooLargeError
                        elif len(account)<8:
                            raise AccountTooSmallError
                        elif len(pw)>20:
                            raise PWTooLargeError
                        elif len(pw)<6:
                            raise PWTooSmallError
                        else:
                            file.write(f"account: {account}\n")   
                            hash_obj = hashlib.sha256(pw.encode())  
                            file.write(f'password:"{pw}" after hash is "{hash_obj.hexdigest()}"\n\n')  
                            file.close()                   
                                                
                    except AccountTooSmallError:
                        print("account too small, please try again 8~12")
                    except AccountTooLargeError:
                        print("account too big, please try again 8~12")
                    except PWTooSmallError:
                        print("password too small, please try again 6~20")
                    except PWTooLargeError:
                        print("password too large, please try again 6~20")
                else:
                    print()
                    break
    else:
        break
 