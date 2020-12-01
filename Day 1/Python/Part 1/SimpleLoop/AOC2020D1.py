



def FileToIntIterable(inputFilename):
    #Takes filename as input(string)
    #Outputs list useful for FindProductSum(iterable with integers)
    with open(inputFilename) as inputFile:
        return [int(x) for x in inputFile.read().split("\n")]




def FindProductSum(wantedSum, inputData):
    #Takes the required sum(int) and list(iterable with integers)
    #Outputs the product(int) of the two numbers which sum to the wantedSum
    #Presumes the given list only has one such set of integers, otherwise only outputs the product of the first set it encounters
    for i in range(len(inputData)):
        if (wantedSum - inputData[i]) in inputData[(i+1):]:
            return ((wantedSum - inputData[i])*inputData[i])
            break
    raise Exception("findProductSum: inputData does not contain two numbers which sum to wantedSum: " + str(wantedSum) + ".")

assert FindProductSum(2020, FileToIntIterable("TestInput.txt")) == 514579

print("Actual Data: " + str(FindProductSum(2020, FileToIntIterable("ActualInput.txt"))))
