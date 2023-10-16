class Contact:
    def __init__(self, name, number, email, address):
        self.name = name
        self.number = number
        self.email = email
        self.address = address


class contactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, number, email, address):
        contact = Contact(name, number, email, address)
        self.contacts.append(contact)
        print(f"Contact '{name}' added successfully.")

    def view_contact_list(self):
        if self.contacts:
            print("\Contact List: ")
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. Name: {contact.name}, number:{contact.number}")
        else:
            print("Contact list is empty!")

    def search_contact(self, query):
        results = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.number:
                results.append(contact)
        if results:
            print("\Search results: ")
            for i, result in enumerate(results, start=1):
                print(f"{i}. Name:{result.name}, Number: {result.number}")
        else:
            print("No matching contacts found!")

    def update_contact(self, index, name, phone, email, address):
        if 0 <= index < len(self.contacts):
            contact = self.contacts[index]
            contact.name = name
            contact.phone = phone
            contact.email = email
            contact.address = address
            print("Contact updated successfully!")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            deleted_contact = self.contacts.pop(index)
            print(f"Contact '{deleted_contact.name}' deleted successfully!")
        else:
            print("Invalid contact index.")


def main():
    contact_book = contactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email address: ")
            address = input("Enter the address: ")
            contact_book.add_contact(name, phone, email, address)

        elif choice == "2":
            contact_book.view_contact_list()

        elif choice == "3":
            query = input("Enter the name or phone number to search: ")
            contact_book.search_contact(query)
        elif choice == "4":
            index = int(input("Enter the index of the contact to update: "))
            name = input("Enter the new name: ")
            phone = input("Enter the new phone number: ")
            email = input("Enter the new email address: ")
            address = input("Enter the new address: ")
            contact_book.update_contact(index - 1, name, phone, email, address)

        elif choice == "5":
            index = int(input("Enter the index of the contact to delete: "))
            contact_book.delete_contact(index - 1)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
