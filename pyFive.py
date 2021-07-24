#Challenge 5
#add_dots() that takes a string and adds "." in between each letter.
#remove_dots removes all dots from a string
def add_dots(str) :
    return '.'.join(str)

def add_dotts(string): #2nd 
    return "".join([a + b for a,b in zip(string,"."*(len(string)-1) +" ")])

def remove_dots(string) :
    return string.replace(".", "")

