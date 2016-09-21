contacts = {}

def create(name, telephone):
    if name not in contacts:
        contacts[name] = telephone
    else:
        raise NameError()

def update(name, telephone):
    if name in contacts:
        contacts[name] = telephone
    else:
        raise NameError()

def delete(name):
    if name in contacts:
        del contacts[name]
    else:
        raise NameError()


def read(name):
    if name in contacts:
        print(name, contacts[name])
    else:
        raise NameError()

while True:
    command = input("""Please enter command:
            #r: read
            #c: create
            #d: delete
            #u: update
            #l: list
            #q: quit
            """)
    if command == "c":
        name = input("Enter new name: ")
        telephone = input("Enter new telephone: ")
        try:
            create(name, telephone)
        except NameError:
            print("Your name already in the contacts")
    elif command == "d":
        name = input("Enter the name of the contact you want to delete: ")
        try:
            delete(name)
        except NameError:
            print("This name is not in your phonebook")
    elif command == "r":
        name = input("Enter the name of the contact you want to read: ")
        try:
            read(name)
        except NameError:
            print("This name is not in your phonebook")
            continue
    elif command == "u":
        name = input("Enter the name of the contact you want to update: ")
        telephone = input("Enter new telephone: ")
        try:
            update(name, telephone)
        except NameError:
            print("This name is not in your phonebook")
    elif command == "l":
        for name, telephone in contacts.items():
            print(name, telephone)
    elif command == "q":
        break
    else:
        print("Try another letter")
