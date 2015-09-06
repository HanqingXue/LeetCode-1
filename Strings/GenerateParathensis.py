#left and right remains are keeping track of how many remaning parthesis left for printing
#current string is used to keep track of current printout for each recursive call

def generate(leftRemain, rightRemain, currentString, listToAdd):
    #first check if there is need to go further
    if rightRemain == 0: #all printed out
        #print(currentString)
        listToAdd.append(currentString)
        return
    #Now coming to the recursive part
    elif (leftRemain > 0): #more left parenthesis left for printing
        #choice 1, print another left bracket
        generate(leftRemain - 1, rightRemain, currentString + "(", listToAdd)
        
        #choice 2 print right bracket if valid
        if leftRemain < rightRemain: #means more left parenthesis have been used
            generate(leftRemain, rightRemain - 1, currentString + ")", listToAdd)
    else: #now there are only right parenthesis left
        generate(leftRemain, rightRemain - 1, currentString+ ")", listToAdd)
        
output = []
print(generate(3,3,"", output))
print(output)
