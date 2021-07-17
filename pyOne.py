def hi(str):
    L= list(str)
    S = []
    for i in range(len(L)):
        if L[i].isupper():
            S.append(i)       
    return S 
