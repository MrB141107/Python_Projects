# Create an empty dictionary to store contacts (name: phone_number)
contacts = {}

def add_contact(name, phone_number):
    contacts[name] = phone_number
    print(f"Contact '{name}' added to the contact list.")

def list_contacts():
    if contacts:
        print("Contacts in the contact list:")
        for name, phone_number in contacts.items():
            print(f"{name}: {phone_number}")
    else:
        print("No contacts in the contact list.")

def search_contact(name):
    if name in contacts:
        print(f"Contact '{name}': {contacts[name]}")
    else:
        print(f"Contact '{name}' not found in the contact list.")

def contact_manager():
    print("Welcome to the Contact Manager application!")

    while True:
        print("\nOptions:")
        print("1. Add contact")
        print("2. List contacts")
        print("3. Search contact")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            name = input("Enter the contact's name: ")
            phone_number = input("Enter the contact's phone number: ")
            add_contact(name, phone_number)
        elif choice == "2":
            list_contacts()
        elif choice == "3":
            name = input("Enter the name to search for: ")
            search_contact(name)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2/3/4).")

if __name__ == "__main__":
    contact_manager()
