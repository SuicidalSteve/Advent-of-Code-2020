



def FileToIntIterable(inputFilename):
    #Takes filename as input(string)
    #Outputs list useful for FindProductSum(iterable with integers)
    with open(inputFilename) as inputFile:
        return [int(x) for x in inputFile.read().split("\n")]




def FindProductSum(wantedSum, inputData):
    #Takes the required sum(int) and list(iterable with integers)
    #Outputs the product(int) of the three numbers which sum to the wantedSum
    #Presumes the given list only has one such set of integers, otherwise only outputs the product of the first set it encounters
    for i in range(len(inputData)):
        for i2 in range(len(inputData[(i+1):])):
            if (wantedSum - inputData[i] - inputData[(i+1):][i2]) in inputData[(i+1):]:
                return ((wantedSum - inputData[i] - inputData[(i+1):][i2])*inputData[i]*inputData[(i+1):][i2])
                break
    raise Exception("findProductSum: inputData does not contain three numbers which sum to wantedSum: " + str(wantedSum) + ".")

assert FindProductSum(2020, FileToIntIterable("TestInput.txt")) == 241861950
print("Test Data: " + str(FindProductSum(2020, FileToIntIterable("TestInput.txt"))))

print("Actual Data: " + str(FindProductSum(2020, FileToIntIterable("ActualInput.txt"))))
