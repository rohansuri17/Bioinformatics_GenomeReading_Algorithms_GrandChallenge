def getReaders(nameOfFile):
    x=0
    reads = []
    with open(nameOfFile) as f:
        for line in f:
			if x%4 == 1:
				reads.append(line.strip())
			x+=1
    return reads
	
rs = getReaders('dataSet1.txt')


def compareTwo(boiMain, sideHoe, comp):
	#str1, str2, comp
	l = len(sideHoe)
	lo = len(boiMain)
	maxx =0
	whereLoc = '-'
	for i in range(comp, l):
		#print(sideHoe[l-i:l])
		if sideHoe[l-i:l] == boiMain[0:i]:
			if maxx < i:
				maxx = i
				whereLoc = 's'
	for j in range(comp, l):
		#hh=l-comp+2
		#while(hh > j):
			#print("", " ")
			#hh-=1
		#print(sideHoe[0:j])
		if sideHoe[0:j] == boiMain[lo-j:lo]:
			if maxx < j:
				maxx = j
				isOnePrefix = False
				whereLoc = 'p'
	return maxx, whereLoc

trueMax =0;
indy =0
for i in range(1, len(rs)):
	maxx, isOnePrefix= compareTwo(rs[100], rs[i], 10)
	if maxx > trueMax:
		trueMax = maxx
		indy = i
print(rs[0])
print(rs[indy])
print(indy)
print(trueMax)



