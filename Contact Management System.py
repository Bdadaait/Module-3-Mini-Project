
import os
import re 
contacts = {}

# Add a new contact
def add_contact(): 
    def add_contact(): 
        identifier = input("Enter a unique identifier (e.g., phone number or email): ") 
        if identifier in contacts:
            print("A contact with this identifier already exists.") 
            return 
        name = input("Enter the name: ") 
        phone = input("Enter the phone number (format: xxx-xxx-xxxx): ") 
        if not re.match(r"^\d{3}-\d{3}-\d{4}$", phone):
            print("Invalid phone number format. Use xxx-xxx-xxxx.")
            return
        email = input("Enter the email address: ") 
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Invalid email format.")
            return 
        
        additional_info = input("Enter additional information (optional): ") 
        contacts[identifier] = {
            "Name": name,
            "Phone": phone, 
            "Email": email, 
            "Additional Info": additional_info, 
        } 
        print("Contact added successfully!")

# Edit an existing contact 
def edit_contact(): 
    identifier = input("Enter the unique identifier of the contact to edit: ") 
    if identifier not in contacts: 
        print("No contact found with this identifier.") 
        return 
    print("Leave fields blank to keep the existing value.") 
    name = input(f"Enter a new name ({contacts[identifier]['Name']}): ") or contacts[identifier]["Name"] 
    phone = input(f"Enter a new phone number ({contacts[identifier]['Phone']}): ") or contacts[identifier]["Phone"] 
    email = input(f"Enter a new email address ({contacts[identifier]['Email']}): ") or contacts[identifier]["Email"] 
    additional_info = input(f"Enter additional information ({contacts[identifier]['Additional Info']}): ") or contacts[identifier]["Additional Info"] 
    contacts[identifier] = {
       "Name": name, 
       "Phone": phone, 
       "Email": email, 
       "Additional Info": additional_info, 
    } 
    print("Contact updated successfully!") 
 
# Delete a contact 
def delete_contact():
  identifier = input("Enter the unique identifier of the contact to delete: ") 
  if identifier in contacts: 
   del contacts[identifier] 
   print("Contact deleted successfully!") 
  else: 
   print("No contact found with this identifier.") 

# Search for a contact 
def search_contact(): 
  identifier = input("Enter the unique identifier of the contact to search: ") 
  if identifier in contacts: 
    print("Contact Details:") 
    for key, value in contacts[identifier].items(): 
        print(f"{key}: {value}") 
    else: 
       print("No contact found with this identifier.")

# Display all contacts 
def display_contacts(): 
  if not contacts: 
    print("No contacts available.") 
    return 
  
  print("All Contacts:") 
  for identifier, details in contacts.items(): 
      print(f"\nIdentifier: {identifier}") 
      for key, value in details.items(): 
          print(f" {key}: {value}") 

# Export contacts to a text file 
def export_contacts(): 
    file_name = input("Enter the name of the file to export to: ") 
    try: 
        with open(file_name , "w") as file: 
            for identifier, details in contacts.items(): 
                file.write(f"Identifier: {identifier}\n") 
                for key, value in details.items(): 
                    file.write(f"{key}: {value}\n") 
                file.write("\n") 
        print(f"Contacts exported successfully to {file_name}!") 
    except Exception as e: 
        print(f"An error occurred while exporting contacts: {e}") 

#  Import contacts from a text file 
def import_contacts(): 
    file_name = input("Enter the name of the file to import from: ") 
    try: 
        with open(file_name, "r") as file: 
           current_contact = {} 
           for line in file: 
               if line.strip() == "":
                  if "Identifier" in current_contact: 
                      contacts[current_contact["Identifier"]] = current_contact 
                      current_contact = {} 
               else: 
                   key, value = line.strip().split(": ", 1) 
                   current_contact[key] = value 
           if "Identifier" in current_contact: 
               contacts[current_contact["Identifier"]] = current_contact 
        print("Contacts imported successfully!") 
    except FileNotFoundError: 
        print("File not found.") 
    except Exception as e: 
        print(f"An error occurred while importing contacts: {e}") 

# Main menu 
def main_menu(): 
  while True: 
    print("\nWelcome to the Contact Management System!") 
    print("1. Add a new contact") 
    print("2. Edit an existing contact") 
    print("3. Delete a contact") 
    print("4. Search for a contact") 
    print("5. Display all contacts") 
    print("6. Export contacts to a text file") 
    print("7. Import contacts from a text file") 
    print("8. Quit") 

    choice = input("Enter your choice (1-8): ") 
    if choice == "1": 
        add_contact() 
    elif choice == "2": 
        edit_contact() 
    elif choice == "3": 
        delete_contact() 
    elif choice == "4": 
        search_contact() 
    elif choice == "5": 
        display_contacts() 
    elif choice == "6": 
        export_contacts() 
    elif choice == "7": 
        import_contacts() 
    elif choice == "8": 
        print("Goodbye!") 
        break 
    else: 
       print("Invalid choice. Please try again.") 


if __name__ == "__main__": 
  main_menu()
