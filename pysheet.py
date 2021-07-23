# #Challenge 4
# # random_number() generate a random integer between 1 and 100, both inclusive, and return it.
# import time
# seconds = time.time()
# x=int(seconds)
# #number of seconds passed since epoch
# # local_time = time.ctime(seconds) #take seoonds as an arguments 
# # print("Local time:", local_time)
# print(seconds) 
# print(type(seconds))
# print(list(x))
import random as rd
# import time 
# print("Printed immediately.")
# time.sleep(2.4)
# print("Printed after 2.4 se
#   L= range(,101)
#   for i in L:
#       x = random()
# seconds = time.time()  
def random_number() :
     return rd.randint(1,100)
#print(random_number())
#isinstance(object, type) function returns True if the specified object is of the specified type, otherwise Fals
# we use type(x) is int for eg and type(23) is int return true 
def only_ints(x,y):
 if type(x) is int and type(y) is int :
    return True  
# print(only_ints(23,35))
    
def only_ins(x,y):
     if type(x) == int and  type(y) == int : 
      return True  
# print(only_ints(23,35))
str = "kdd"
L = list(str)
print(type(L))
L.remove(L[0])
print(L)
print("L[0]" in L)
