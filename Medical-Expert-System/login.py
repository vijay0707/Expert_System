import module 
# from medical_expert_system import preprocess, Greetings
users = {}
status = ""
# prep = preprocess()
# engine = Greetings()

class Login():
    def displayMenu(self):
        status = input("Are you registered user? y/n? Press q to quit")
        if status == "y":
            self.oldUser()
        elif status == "n":
            self.newUser()


    def newUser(self):
        createLogin = input("Create login name: ")

        if createLogin in users:
            print("\nLogin name already exist!\n")
        else:
            createPassw = input("Create password: ")
            users[createLogin] = createPassw
            print("\nUser created\n")


    def oldUser(self):
        login = input("Enter login name: ")
        passw = input("Enter password: ")

        if login in users and users[login] == passw:
            print("\nLogin successful!\n")

            return module.main()

	                

        else:
            print("\nUser doesn't exist or wrong password!\n")


log = Login()

while status != "q":
    log.displayMenu()

    