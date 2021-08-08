#Challenge 10
#Tic tac toe input
def get_row_col(str) :
    return (["1","2","3"].index(str[1]) , ["A", "B", "C"].index(str[0]))

print(get_row_col("C2")) 