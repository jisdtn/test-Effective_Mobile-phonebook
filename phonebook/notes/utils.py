from typing import List

from models import Contact


def read_contactsList(filename: str) -> List:
    """Shows the list of Contacts."""
    contacts = []
    with open(filename, 'r') as file:
        for line in file:
            contact_data = line.strip().split(',')
            contact = Contact(*contact_data)
            contacts.append(contact)
    return contacts


def write_contacts(filename: str, contacts: List) -> None:
    """Writes data to a file."""
    with open(filename, 'a') as file:
        for contact in contacts:
            file.write(f"{contact.last_name},{contact.first_name},"
                       f"{contact.middle_name},{contact.organization},"
                       f"{contact.work_phone},{contact.personal_phone}\n")


def add_contact(filename: str, contact: Contact) -> None:
    """Adds a Contact object to a contact list."""
    contacts = read_contactsList(filename)
    contacts.append(contact)
    write_contacts(filename, contacts)


def edit_contact(filename: str):
    contacts = read_contactsList(filename)
    print("Enter the details of the contact you want to edit:")
    last_name = input("Last Name: ")
    first_name = input("First Name: ")
    middle_name = input("Middle Name: ")

    found_contacts = []
    for contact in contacts:
        if contact.last_name == last_name and \
                contact.first_name == first_name and \
                contact.middle_name == middle_name:
            found_contacts.append(contact)

    if not found_contacts:
        print("Contact not found.")
        return

    if len(found_contacts) > 1:
        print("Multiple contacts found. Please refine your search.")
        return

    contact = found_contacts[0]
    print("Contact found. Enter the new details:")

    contact.last_name = input(f"Last Name "
                              f"({contact.last_name}): ") or contact.last_name
    contact.first_name = input(
        f"First Name {contact.first_name}: "
    ) or contact.first_name
    contact.middle_name = input(
        f"Middle Name {contact.middle_name}): "
    ) or contact.middle_name
    contact.organization = input(
        f"Organization {contact.organization}): "
    ) or contact.organization
    contact.work_phone = input(
        f"Work Phone ({contact.work_phone}): "
    ) or contact.work_phone
    contact.personal_phone = input(
        f"Personal Phone {contact.personal_phone}): "
    ) or contact.personal_phone

    write_contacts(filename, contacts)
    print("Contact edited successfully!")


def searchInPhonebook(filename: str, **kwargs: object) -> List:
    """Searches in the list by all the model attributes."""
    contacts = read_contactsList(filename)
    found_contacts = []
    for contact in contacts:
        if all(getattr(contact, attr) == value
               for attr, value in kwargs.items()):
            found_contacts.append(contact)
    return found_contacts
