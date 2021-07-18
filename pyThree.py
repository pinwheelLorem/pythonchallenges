# Challenge 3
# online_count , on_ count return the number of ppl who are online in a dictionary

def online_count(dict):
    S = 0
    for x in dict.values():
        if x == "online" :
            S += 1
    return S         
    
def on_count(dict):
    return len([ x for x in dict.values() if x == "online" ])

dict = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
 
print(on_count(dict))
print(online_count(dict))