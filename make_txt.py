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

#remember to close file

address = os.getcwd()
count=0


while True:
    
    try:
        name = input("filename: ")
            
        if  os.path.isfile(f"{name}.txt"):
            raise FileAlreadyExists
            
        elif name=='stop':
            break    
        else:
            print("File not existed, creating file...")
            file = open(f"{address}\\{name}.txt", 'w')
            pass
            
    except FileAlreadyExists:
        print("File already exists, please try again")
        
    while True:
        try:
            file = open(f"{address}\\{name}.txt", 'w')
            account=input("account name: ")
            if len(account)<8:
                raise AccountTooSmallError
            elif len(account)>12:
                raise AccountTooLargeError
            elif account=='stop':
                break
            else:
                file.write(f"account: {account}\n")
                break
                
                
                    
            
        except AccountTooSmallError:
            print("account too small, please try again 8~12")
        except AccountTooLargeError:
            print("account too big, please try again 8~12")

        
    while True:
        try:
            #file = open(f"{address}\\{name}.txt", 'w')
            pw = input("password: ")
            if len(pw)<6:
                raise PWTooSmallError
            elif len(pw)>20:
                raise PWTooLargeError
            elif pw=='stop':
                break
            else:
                    
                outFileName = f'{name}.txt'
                with open(outFileName, mode='a+') as outFile_obj:
                    hash_obj = hashlib.sha256(pw.encode())
                    outFile_obj.write(hash_obj.hexdigest())
                    
                    file.write(f'"password: {pw}" after hash is "{hash_obj.hexdigest()}"')
                    outFile_obj.close()
                    file.close()
                break
        except PWTooSmallError:
            print("password too small, please try again 6~20")
        except PWTooLargeError:
            print("password too large, please try again 6~20")

            

