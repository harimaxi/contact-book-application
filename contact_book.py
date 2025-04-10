import os

CONTACTS_FILE = "contacts.txt"

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    with open(CONTACTS_FILE, "a") as file:
        file.write(f"{name},{phone},{email}\n")
    print("✅ Contact added successfully!\n")

def view_contacts():
    if not os.path.exists(CONTACTS_FILE) or os.path.getsize(CONTACTS_FILE) == 0:
        print("📭 No contacts found.\n")
        return

    print("\n📒 Contact List:")
    with open(CONTACTS_FILE, "r") as file:
        for i, line in enumerate(file, 1):
            name, phone, email = line.strip().split(",")
            print(f"{i}. Name: {name}, Phone: {phone}, Email: {email}")
    print()

def search_contact():
    keyword = input("Enter name or phone to search: ").strip().lower()

    found = False
    with open(CONTACTS_FILE, "r") as file:
        for line in file:
            name, phone, email = line.strip().split(",")
            if keyword in name.lower() or keyword in phone:
                print(f"🔍 Found: Name: {name}, Phone: {phone}, Email: {email}")
                found = True
    if not found:
        print("❌ Contact not found.\n")
    print()

def main():
    while True:
        print("📇 Contact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
