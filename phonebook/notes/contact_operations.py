from .models import Contact


def read_contactsList(filename):
    contacts = []
    with open(filename, 'r') as file:
        for line in file:
            contact_data = line.strip().split(',')
            contact = Contact(*contact_data)
            contacts.append(contact)
    return contacts

def write_contacts(filename, contacts):
    with open(filename, 'a') as file:
        for contact in contacts:
            file.write(f"{contact.last_name},{contact.first_name},"
                       f"{contact.middle_name},{contact.organization},"
                       f"{contact.work_phone},{contact.personal_phone}\n")

def add_contact(filename, contact):
    contacts = read_contactsList(filename)
    contacts.append(contact)
    write_contacts(filename, contacts)

def edit_contact(filename, edited_contact):
    contacts = read_contactsList(filename)
    for i, contact in enumerate(contacts):
        if contact.last_name == edited_contact.last_name and \
                contact.first_name == edited_contact.first_name and \
                contact.middle_name == edited_contact.middle_name:
            contacts[i] = edited_contact
            break
    write_contacts(filename, contacts)


def searchInPhonebook(filename, **kwargs):
    contacts = read_contactsList(filename)
    found_contacts = []
    for contact in contacts:
        if all(getattr(contact, attr) == value for attr, value in kwargs.items()):
            found_contacts.append(contact)
    return found_contacts
