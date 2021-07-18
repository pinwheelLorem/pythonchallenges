#Challenge 1
#Middle letter 
#hi function return the position of all the uppercase character in a string.

def hi(str):
    L= list(str)
    S = []
    for i in range(len(L)):
        if L[i].isupper():
            S.append(i)       
    return S 
