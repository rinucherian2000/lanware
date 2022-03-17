def uppercase(fun):

    def wrapper():

        res = fun()
        modified = res.upper()

        return modified
    return wrapper

@uppercase
def toupper():
    return 'uppercase'

message = toupper()
print(message)
