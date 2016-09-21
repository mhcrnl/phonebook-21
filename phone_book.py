contacts = {}


def create_instance():
    name = input("Enter new name: ")
    telephone = input("Enter new telephone: ")
    try:
        create(name, telephone)
    except NameError:
        print("Your name already in the contacts")


def update_instance():
    name = input("Enter the name of the contact you want to update: ")
    telephone = input("Enter new telephone: ")
    try:
        update(name, telephone)
    except NameError:
        print("This name is not in your phonebook")


def delete_instance():
    name = input("Enter the name of the contact you want to delete: ")
    try:
        delete(name)
    except NameError:
        print("This name is not in your phonebook")


def read_instance():
    name = input("Enter the name of the contact you want to read: ")
    try:
        read(name)
    except NameError:
        print("This name is not in your phonebook")


def list_instances():
    if contacts:
        for name, telephone in contacts.items():
            print(name, telephone)
    else:
        print("There are no contacts in the phonebook")


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
        create_instance()
    elif command == "d":
        delete_instance()
    elif command == "r":
        read_instance()
    elif command == "u":
        update_instance()
    elif command == "l":
        list_instances()
    elif command == "q":
        break
    else:
        print("Try another letter")
