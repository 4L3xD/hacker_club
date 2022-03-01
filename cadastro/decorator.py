def uppercase_decorator(func):
    def wrapper():
        #return func.upper()
        return func().upper()
    return wrapper

#def say_hi():
#    return 'hello there'
#
#decorate = uppercase_decorator(say_hi())
#print(decorate())

@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi())

#In: https://www.datacamp.com/community/tutorials/decorators-python

