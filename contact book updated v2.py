import json

FILE_NAME = "contacts.json"

try:
    with open(FILE_NAME, "r") as file:
        contacts = json.load(file)
except:
    contacts = []


def save_contacts():

    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact():

    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    for existing_contact in contacts:

        if existing_contact["name"].lower() == name.lower():
            print("Contact already exists!")
            return

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)

    save_contacts()

    print("Contact Added Successfully!")


def view_contacts():

    if len(contacts) == 0:
        print("No contacts found.")
        return

    sorted_contacts = sorted(
        contacts,
        key=lambda contact: contact["name"].lower()
    )

    print("\n===== CONTACT LIST =====")

    for contact in sorted_contacts:

        print("--------------------------")
        print("Name   :", contact["name"])
        print("Phone  :", contact["phone"])
        print("Email  :", contact["email"])
        print("Address:", contact["address"])


def search_contact():

    name = input("Enter name to search: ")

    for contact in contacts:

        if contact["name"].lower() == name.lower():

            print("Contact Found!")
            print("Name   :", contact["name"])
            print("Phone  :", contact["phone"])
            print("Email  :", contact["email"])
            print("Address:", contact["address"])

            return

    print("Contact not found.")


def search_by_phone():

    phone = input("Enter phone number: ")

    for contact in contacts:

        if contact["phone"] == phone:

            print("Contact Found!")
            print("Name   :", contact["name"])
            print("Phone  :", contact["phone"])
            print("Email  :", contact["email"])
            print("Address:", contact["address"])

            return

    print("Contact not found.")


def edit_contact():

    name = input("Enter contact name to edit: ")

    for contact in contacts:

        if contact["name"].lower() == name.lower():

            print("Leave blank to keep old value.")

            new_name = input("New Name: ")
            new_phone = input("New Phone: ")
            new_email = input("New Email: ")
            new_address = input("New Address: ")

            if new_name:
                contact["name"] = new_name

            if new_phone:
                contact["phone"] = new_phone

            if new_email:
                contact["email"] = new_email

            if new_address:
                contact["address"] = new_address

            save_contacts()

            print("Contact Updated Successfully!")
            return

    print("Contact not found.")


def delete_contact():

    name = input("Enter contact name to delete: ")

    for contact in contacts:

        if contact["name"].lower() == name.lower():

            contacts.remove(contact)

            save_contacts()

            print("Contact Deleted Successfully!")
            return

    print("Contact not found.")



while True:

    print("""
========== CONTACT BOOK ==========

1. Add Contact
2. View Contacts
3. Search By Name
4. Search By Phone
5. Edit Contact
6. Delete Contact
7. Exit

==================================
""")

    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        search_by_phone()

    elif choice == "5":
        edit_contact()

    elif choice == "6":
        delete_contact()

    elif choice == "7":
        print("Goodbye!")
    break

else:
    print("Invalid choice.")