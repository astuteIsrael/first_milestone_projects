from tabulate import tabulate

phone_book = [
    {"name": "Winnie", "phone_number": "09030556547", "favorite": False}

]

def add_contact():
    name = input("Enter the contact's name: ")
    phone_number = input("Enter the contact's phone number: ")
    phone_book.append({"name": name, "phone_number": phone_number, "favorite": False})
    print("Contact added successfully")

def view_contacts():
    table = []
    heading = ["S/N", "Name", "Phone Number", "Favorite"]

    table.append(heading)
    for index, contact in enumerate(phone_book, start=1):
        table.append([index, contact["name"], contact["phone_number"], contact["favorite"]])       

    print(tabulate(table, tablefmt="fancy_grid"))


def update_contact(phone_number):

    for contact in phone_book:
        if contact["phone_number"] == phone_number:
            name = input(f"Enter the new name for {contact["name"]}. Leave blank to use {contact["name"]}: ").strip()
            phone_num = input(f"Enter the new phone number for {contact["phone_number"]}. Leave blank to use {contact["phone_number"]}: ").strip()
            if name:
                contact["name"] = name
            if phone_num:
                contact["phone_number"] = phone_num
            return f"Contact updated successfully."
    return "Contact with that phone number does not exist"


def delete_contact(phone_number):
    for contact in phone_book:
        if contact["phone_number"] == phone_number:
            phone_book.remove(contact)
            return f"Contact deleted successfully."
    return "Contact with that phone number does not exist"


def search_contact(phone_number):
 
    for contact in phone_book:
        if contact["phone_number"] == phone_number:
            contact = f"""
Found:
Name: {contact["name"]}
Phone number: {contact["phone_number"]}
"""
            return contact
    return "Contact with that phone number does not exist" 


def mark_favorite(phone_number):
    for contact in phone_book:
        if contact["phone_number"] == phone_number:
            if contact["favorite"]:
                return f"Contact {contact["name"]} is already a favorite"
            contact["favorite"] = True
            return f"Contact {contact["name"]} is now a favorite."
    return "Contact with that phone number does not exist"    


def unmark_favorite(phone_number):
    for contact in phone_book:
        if contact["phone_number"] == phone_number:
            if not contact["favorite"]:
                return f"Contact {contact["name"]} is already not a favorite"
            contact["favorite"] = False
            return f"Contact {contact["name"]} is no longer a favorite."
    return "Contact with that phone number does not exist"    

menu = """
1. Add Contact.
2. View Contacts.
3. Update Contact.
4. Delete Contact.
5. Search Contact.
6. Mark as Favorite.
7. Unmark as Favorite.
8. Quit.
"""

while True:
    print(menu)
    choice = input("Choose an option from the menu above: ").strip()

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        phone_number = input("Enter the phone number of the contact you wish to update: ").strip()
        print(update_contact(phone_number))
    elif choice == "4":
        phone_number = input("Enter the phone number of the contact you wish to delete: ").strip()
        print(delete_contact(phone_number))
    elif choice == "5":
        phone_number = input("Enter the phone number of the contact you wish to search for: ").strip()
        print(search_contact(phone_number))
    elif choice == "6":
        phone_number = input("Enter the phone number of the contact you wish to mark as favorite: ").strip()
        print(mark_favorite(phone_number))
    elif choice == "7":
        phone_number = input("Enter the phone number of the contact you wish to unmark as favorite: ").strip()
        print(unmark_favorite(phone_number))
    elif choice == "8":
        print("goodbye")
        break
    else:
        print("Enter a valid choice form the menu")

