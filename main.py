from Manager import Manager
def menu():
    print("pick an option:")
    print("1. generate password")
    print("2. update password")
    print("3. delete pasword")
    print("4.get password")
    print("5. Quit")
    choice=input("enter option:")
    return choice
def generate_pass(m):
    site=input("enter site name:")
    usr=input("enter username:")
    length=input("password length")
    print("password:"+m.generate_password(site,usr,length))
def get_pass(m):
    site=input("enter site:")
    usr=input("enter usrname:")
    print("username:",usr)
    print("password:",m.get_get_password(site,usr))
def delete(m):
    site=input("enter site:")
    usr=input("enter username:")
    m.delete(site,usr)
PIN="0000"
def login():
    while True:
        p=input("enter PIN: ")
        if p==PIN:
            break
def update(m):
    site=input("Enter site")
    usr=input("Enter user")
    p=input("Enter new pass")
    m.update(site,usr,p)
    print("password updates")
de f main():
    login()
    m=Manager()
    m.load()
    while True:
        choice=menu()
        if choice==1:
            generate_pass(m)
        elif choice==2:
            update(m)
        elif choice==3:
            delete(m)  
        elif choice==4:
            get_pass(m) 
        else:
            m.save()
            break
            )
            
            )

main()
    