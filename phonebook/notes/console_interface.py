from typing import Dict

from models import Contact
from utils import read_contactsList, add_contact, edit_contact, searchInPhonebook


def console_interface() -> None:
    """Console interface logic."""
    print("Welcome to the Phonebook!")

    filename: str = 'notes/data.txt'

    while True:
        print("\nMenu:")
        print("1. View contacts")
        print("2. Add a new contact")
        print("3. Edit a contact")
        print("4. Search for contacts")
        print("5. Exit")

        choice: str = input("Enter your choice: ")

        if choice == '1':
            contacts = read_contactsList(filename)
            for contact in contacts:
                print(contact)
        elif choice == '2':
            last_name: str = input("Enter last name: ")
            first_name: str = input("Enter first name: ")
            middle_name: str = input("Enter middle name: ")
            organization: str = input("Enter organization: ")
            work_phone: str = input("Enter work phone: ")
            personal_phone: str = input("Enter personal phone: ")
            new_contact = Contact(last_name, first_name, middle_name, organization, work_phone, personal_phone)
            add_contact(filename, new_contact)
            print("Contact added successfully!")
        elif choice == '3':
            last_name: str = input("Enter last name: ")
            first_name: str = input("Enter first name: ")
            middle_name: str = input("Enter middle name: ")
            organization: str = input("Enter organization: ")
            work_phone: str = input("Enter work phone: ")
            personal_phone: str = input("Enter personal phone: ")
            edited_contact = Contact(last_name, first_name, middle_name, organization, work_phone, personal_phone)
            edit_contact(filename, edited_contact)
            print("Contact edited successfully!")
        elif choice == '4':
            last_name: str = input("Enter last name (press Enter to skip): ")
            first_name: str = input("Enter first name (press Enter to skip): ")
            middle_name: str = input("Enter middle name (press Enter to skip): ")
            organization: str = input("Enter organization (press Enter to skip): ")
            work_phone: str = input("Enter work phone (press Enter to skip): ")
            personal_phone: str = input("Enter personal phone (press Enter to skip): ")
            search_criteria: Dict[str, str] = {}
            if last_name:
                search_criteria['last_name'] = last_name
            if first_name:
                search_criteria['first_name'] = first_name
            if middle_name:
                search_criteria['middle_name'] = middle_name
            if organization:
                search_criteria['organization'] = organization
            if work_phone:
                search_criteria['work_phone'] = work_phone
            if personal_phone:
                search_criteria['personal_phone'] = personal_phone
            found_contacts = searchInPhonebook(filename, **search_criteria)
            if found_contacts:
                for contact in found_contacts:
                    print(contact)
            else:
                print("No matching contacts found.")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    console_interface()
