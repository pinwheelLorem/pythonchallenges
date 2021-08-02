#Challenge 7 
#is_anagram takes two strings as its parameters.It returns True if the strings are anagrams, and False otherwise.

def is_anagram(a,b):
    L=list(a)
    M=list(b)
    if len(L)==len(M):
        for i in range(len(L)):
            if L[0] in M:
                M.remove(L[0])
                L.pop(0)
            else:
                return False
        return True 
    return False   

def isanagram(a,b):
    return sorted(a)==sorted(b)   

def counting(a): 
    return {l: a.count(l) for l in a}

def isanagramm(a,b):
    return counting(a) == counting(b)