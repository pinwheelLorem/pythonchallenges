#Challenge 4
#Define a function named double_letters that takes a single parameter. 
def double_letters(str):
  L= list(str)
  for i in range(len(L)-1) :
       if L[i] == L[i+1] :
           return True                      
  return False  

def doubl_letters(L):
  for i in range(len(L)-1) :
       if L[i] == L[i+1] :
           return True                      
  return False            

def db_letters(str) : #2nd
    return any([a == b for a,b in zip(str,str[1:])]) 
 