#step 1 decide how many elements in a sub array to be printed

def subsets(nums):


#step 2, this mothod proccsed the action to print out all possible combinations of elements  with fixed size
#as dicussed we need three additional variables to keep track of status
#boolean array to know whether printed out or not,
#start is the start index to be printed to prevent duplicates
#remain is keeping track of how many remaining elements to be processedfor the subset action

def PrintSubSet(nums, ifPrinted, start, remain):
    # firstly if remain == 0, we're done
    if remain == 0:
        #check ifPrint status to decide print or not
        for i in range(len(ifPrint)):
            if ifPrint[i]:
                print(nums[i] + ",")
        print(")
