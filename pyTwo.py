
#Challenge 2
#Middle letter
#mid that takes a string as its parameter.Return the middle letter. If there is no middle letter,it'll return the empty string.
        
def mid(str) :
    L = list(str)
    n = len(L)
    print(L)
    while n > 1:
     for i in range(n):
        if n%2 != 0:
            return L[n//2] 
        return ''