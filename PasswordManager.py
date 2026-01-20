from cryptography.fernet import Fernet
# Create a key file Once
'''
def createkey():
        key = Fernet.generate_key()
        with open("key.key",'wb') as key_file:
                key_file.write(key)
                '''

def load_key():
        with open("key.key",'rb') as file:
                return file.read()
key = load_key()
fern = Fernet(key)
def view_pass():
        while True:
                search = input("Enter Username:")
                if search.lower() == "quit":
                        break
                found = False
                with open("password.txt","r") as f:
                        for line in f.readlines():
                                data = line.rstrip()
                                user,password = data.split("||")
                                if(search==user):
                                        print("PASSWORD: ",fern.decrypt(password.encode()).decode())
                                        found = True
                                        break
                                        
                                
                        if found:
                                print("Invalid Username")
                
                

def add_pass():
            Acc_Name = input("Account Name: ")
            Password = input("Enter Pass: ")

            with open("password.txt" ,'a') as f:
                    f.write(Acc_Name + "||" + fern.encrypt(Password.encode()).decode() +"\n")

while True:
        user_choice = input("TO VIEW EXISTING PASSES(Enter V) , TO ADD A NEW PASS(Enter A) , TO QUIT(Enter Q): ").strip().lower()
        if user_choice=="q":
                break
        if user_choice == "v":
                view_pass()
        elif user_choice == "a":
                add_pass()
                print("New Password Saved In password.txt")
        else:
                continue


