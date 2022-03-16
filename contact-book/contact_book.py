import sqlite3

# name, address, phone number, and even email address

with sqlite3.connect(r".\\beginner projects\\contact-book\\contacs_book.db") as sc:

    try:
        sc.execute("""\
            CREATE TABLE Contact(
                Id int primary key not null,
                Name text not null,
                Address char(50),
                Phone_number int not null,
                Email text not null
            )
        """)
    except sqlite3.OperationalError:
        pass

    while True:
        print("""\
        1. Save new contact
        2. Update contact
        3. List saved contacts
        4. Exit

        """)

        user_input = input("Select an option (1|2|3|4) >>> ")

        if user_input == "1":
            id = int(input("Enter the contact's id > "))
            name = input("Enter the contact's name > ")
            address = input("Enter the contact's address > ")
            phone = int(input("Enter the contact's phone number > "))
            email = input("Enter the contact's email > ")

            execute = f"INSERT INTO Contact (Id, Name, Address, Phone_number, Email) VALUES ({id}, '{name}', '{address}', {phone}, '{email}')"
            sc.execute(execute)
            print("contact has been saved successfully!")

        if user_input == "2":
            to_update = input("Enter the item you wanna change (id|name|address|phone|email) > ")
            if to_update == "id" or to_update == "phone":
                value = int(input("Enter the new value to " + to_update + " item > "))
            else:
                value = input("Enter the new value to " + to_update + " item > ")  
                value = "'"+value+"'"              
            contact_id = int(input("Enter the contact's id > "))

            sc.execute("UPDATE Contact SET " + to_update + " = " + str(value) + " WHERE Id = " + str(contact_id))
            print()
            print("Item updated successfully!")

        if user_input == "3":
            contacts = sc.execute("SELECT * FROM Contact")
            for contact in contacts:
                print(f"Id: {contact[0]}")
                print(f"Name: {contact[1]}")
                print(f"Address: {contact[2]}")
                print(f"Phone number: {contact[3]}")
                print(f"Email: {contact[4]}")
        elif user_input == "4":
            break



        