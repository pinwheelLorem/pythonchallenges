 
Name = input("Enter your full name: ")
Number = int(input("Enter your number 9 digits: "))
EmailValue = input("Enter your email adress :")
AdressValue = input("Enter your home adress :")
file=[Number, EmailValue, AdressValue]
dict = {Name:file}

ddu = input("Enter name: ")
print(f"Number of {ddu}:{dict[ddu][0]}")
print(f"Email adress of {ddu}: {dict[ddu][1]}")
print(f"Home adress of {ddu}: {dict[ddu][2]}")
