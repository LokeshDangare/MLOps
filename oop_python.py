class Chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.logged_in = False
        self.menu()

    def menu(self):
        user_input = input(""" Welcome to Chatbook !! 
                           1. press 1 to Sign Up
                           2. press 2 to Sign In
                           3. press 3 to write a post
                           4. press 4 to message a friend
                           5. press anykey to exit""")
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.post()
        elif user_input == "4":
            self.msg()
        else:
            exit()

    
    def signup(self):
        email = input("Enter your email: ")
        pwd = input("Enter your password: ")
        self.username = email
        self.password = pwd
        print("Sign up successful!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == "" and self.password == "":
            print("You have to sign up first")
        else:
            uname = input("Enter your email: ")
            pwd = input("Enter your password: ")
            if self.username == uname and self.password == pwd:
                print("Sign in successful!")
                self.logged_in = True
            else:
                print("Invalid credentials!")
        print("\n")
        self.menu()

    def post(self):
        if self.logged_in == True:
            txt = input("Enter your message here: ")
            print(f"Your following content will be posted: {txt}")
        else:
            print("You need to sign in first")
        print("\n")
        self.menu()

    def msg(self):
        if self.logged_in == True:
            txt = input("Enter your message here: ")
            friend = input("Whom to send the message to: ")
            print(f"Ypur message will be sent to {friend}")
        else:
            print("You need to sign in first")
        print("\n")
        self.menu()

obj = Chatbook()