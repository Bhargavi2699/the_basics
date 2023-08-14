#slice the username, domain and extension
#collect email from the user
#split the email using @, you end up getting username and domain
#split the domain using '.'

def main():
    print("Welcome to email slicer.")
    print()

    email_input = input("Enetr your email address: ")

    username,domain = email_input.split("@")
    domain, extension = domain.split(".")

    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)

while True:
    main()