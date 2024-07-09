contacts = []
while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    if choice == '1':
        print("\nAdd Contact:")
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        address = input("Enter address: ")
        contact = {'name': name, 'phone': phone, 'email': email, 'address': address}
        contacts.append(contact)
        print("Contact added successfully!")
    elif choice == '2':
        print("\nContact List:")
        if not contacts:
            print("No contacts found.")
        else:
            for index, contact in enumerate(contacts):
                print(f"{index + 1}. Name: {contact['name']}, Phone: {contact['phone']}")
    elif choice == '3':
        print("\nSearch Contact:")
        search_term = input("Enter name or phone number to search: ")
        found = False
        for contact in contacts:
            if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
                print(f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}")
                found = True
        if not found:
            print("Contact not found.")
    elif choice == '4':
        print("\nUpdate Contact:")
        search_term = input("Enter name or phone number of the contact to update: ")
        found = False
        for contact in contacts:
            if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
                print(f"Updating contact: {contact['name']}")
                contact['name'] = input("Enter new name (press enter to keep current): ") or contact['name']
                contact['phone'] = input("Enter new phone number (press enter to keep current): ") or contact['phone']
                contact['email'] = input("Enter new email address (press enter to keep current): ") or contact['email']
                contact['address'] = input("Enter new address (press enter to keep current): ") or contact['address']
                print("Contact updated successfully!")
                found = True
        if not found:
            print("Contact not found.")
    elif choice == '5':
        print("\nDelete Contact:")
        search_term = input("Enter name or phone number of the contact to delete: ")
        found = False
        for contact in contacts:
            if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
                print(f"Deleting contact: {contact['name']}")
                contacts.remove(contact)
                print("Contact deleted successfully!")
                found = True
        if not found:
            print("Contact not found.")
    elif choice == '6':
        print("Contact Book is Exited. Goodbye!")
        break
    else:
        print("Try again. Please enter a number between 1 and 6.")
