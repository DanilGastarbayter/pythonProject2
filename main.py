print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
try:
    print('start code')
    print('no errors')
except NameError:
    print("We have an error nameerror ")
except ZeroDivisionError:
    print("We have an error zerodivisionerror ")
print('The end')
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
try:
    print('start code')
    print(5/0)
    print('no errors')
except (NameError, ZeroDivisionError) as error:
    print("error")
print('The end')
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
try:
    try:
        print('start code')
        print(error)
        print('no error')
    except SyntaxError:
        print("Wrong Syntax")
except NameError as error:
    print(error)