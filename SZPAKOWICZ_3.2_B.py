### This is an extension of file 3.2 - standard Binary Search ###

#Binary Search function
#Takes two input parameters -  a text file and a int value
#Searches for the value within the text file using a binary search algorithm
#Returns the numbers of comparisons done and the index position of the value
#(or -1 if not found)
def biSearch(file, value):
    nList = list(map(int, file.read().split()))
    vList = list(map(int, value.read().split()))
    comparisons = 0
    position = 0 #acts like the middle in this algorithm
    pos = 0
    low = 0
    high = len(nList) - 1

    ###BENCHMARK DATA###
    mini = 0
    average = 0
    ####################

    #Binary search keeps splitting the list in half
    #Depending on where the value is located, low or high are changed
    while len(vList) > pos:
        while low <= high:
            comparisons+=1
            position = (high + low)//2
            if nList[position] == vList[pos]:
                break
            elif nList[position] > vList[pos]:
                high = position - 1 #if value is lower than current number at index
            else:
                low = position + 1 #if value is greater than current number at index

        if mini == 0:
            mini = comparisons
        average = average + comparisons
        pos+=1 #index of vList: each number being searched for
        low = position #List cuts out everything before current number
        high = len(nList) -1 #End of list remains the same
        
    #BENCHMARK DATA RESULTS     
    average = int(average / comparisons)
    print(mini, average, comparisons)
    return True

#Driver for testing
file = open("benchmark_data.txt", "r")
value = open("benchmark_search_values.txt", "r")
print("###BENCHMARK RESULTS###")
print("\nMin, Average, Max:")
biSearch(file, value)
file.close()
