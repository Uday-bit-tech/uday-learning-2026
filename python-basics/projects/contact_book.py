contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        number = input("Enter Mobile Number: ")
        contacts[name] = number
        print("Contact Added!")

    elif choice == "2":
        print("\nContacts List:")
        for name, number in contacts.items():
            print(name, ":", number)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")
