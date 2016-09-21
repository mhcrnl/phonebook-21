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
