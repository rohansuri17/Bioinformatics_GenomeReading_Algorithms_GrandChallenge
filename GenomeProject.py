def getReaders(nameOfFile):
    x=0
    reads = []
    with open(nameOfFile) as f:
        for line in f:
            if x%4 == 1:
                reads.append(line.strip())
            x+=1
    return reads

reader = getReaders('dataSet1_small.txt')
print (reader)

def findSubstringInArray(suffix, prefix, array):
    #only check if overlap prefixes and suffixes
    matchIndexes = []
    matchValues= []
    #substring
    length = len(suffix)
    for i in range(len(array)):
        #read= prefix, substring = suffix
        if (array[i][0:length] == suffix):
            #TODO: should I concatenate into contigs here already? 
            matchIndexes.append((i,"s)"))
            matchValues.append((array[i], "p"))
        elif (array[i][: -length] == prefix):
            matchIndexes.append((i, "p"))
            matchValues.append((array[i], "p"))
    print("S:", suffix, "P:", prefix, matchValues )
    return matchIndexes
    

def AssemblyAlgorithm(): #its ok dudley wrote this
    readArray= getReaders('dataSet1_small.txt') #for reads
    #lengthArray= [ ] 
    #array of readStrings
    for i in range(len(readArray)): 
        readItem= readArray[i]
        readLength = len(readItem)
        n = 2	#first try to match 50% of read
        foundSubstringCount = -1
        while( foundSubstringCount < 0 or len(readItem[0:int(readLength/n)])< 5 ): 
            #while not found match at current substring length, or comparing at length 5, which is minimum bar
            len_match= readLength/n
            prefix =  readItem[0:int(len_match)]
            suffix = readItem[:-int(len_match)] #match from end
            #returns the indexes in the array of the read to which the substring matched
            #if a read matched to only one it's more likely to be the true match to that one as opposed to a read that matched to 5
            foundSubstringIndexes = findSubstringInArray( prefix, suffix, readArray )
            foundSubstringCount = len(foundSubstringIndexes) #will exit loop when found matching reads
            n+= 1  #decrease substring percentage match
