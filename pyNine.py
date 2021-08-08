#Challenge 9
#largest_difference takes a list of numbers as its only parameter computes and returns the difference between the largest and smallest number in the list.
 
def largest_difference(L):
    return sorted(L)[-1] - sorted(L)[0]
print(largest_difference([2,53,1,9]))