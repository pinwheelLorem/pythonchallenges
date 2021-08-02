#Challenge 8
#flatten takes a list of lists and flattens it into a one-dimensional list.
def flatten(L):
    return [ elm  for l in L for elm in l]  
      
