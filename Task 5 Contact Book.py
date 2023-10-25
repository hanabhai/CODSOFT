# Code done by Ameer Hamza
class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = {"name": name, "phone": phone, "email": email, "address": address}
        self.contacts.append(contact)
        print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\n--- Contact List ---")
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact['name']} - {contact['phone']}")
            print("--------------------")

    def search_contact(self, search_term):
        found_contacts = []
        for contact in self.contacts:
            if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
                found_contacts.append(contact)
        if found_contacts:
            print("\n--- Search Results ---")
            for i, contact in enumerate(found_contacts, 1):
                print(f"{i}. {contact['name']} - {contact['phone']}")
            print("-----------------------")
        else:
            print("No contacts found matching the search term.")

    def update_contact(self, search_term, name, phone, email, address):
        for contact in self.contacts:
            if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
                contact['name'] = name
                contact['phone'] = phone
                contact['email'] = email
                contact['address'] = address
                print("Updated Successfully")
                return
        print("Not any Contact  found.")

    def delete_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Not any Contact  found.")


def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)
        elif choice == '4':
            search_term = input("Enter name or phone number to update: ")1
            name = input("Enter new name: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contact_book.update_contact(search_term, name, phone, email, address)
        elif choice == '5':
            search_term = input("Enter name or phone number to delete: ")
            contact_book.delete_contact(search_term)
        elif choice == '6':
            print("Ending ")
            break
        else:
            print("Invalid Selection.... Please enter a valid option.")


if __name__ == "__main__":
    main()
