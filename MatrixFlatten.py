import itertools
# x = [[['foo', 'foo2'], ['foo', 'foo2']], [['bar', 'bar2'], ['baz', 'baz2']], [['quux', 'quux2'], ['quux', 'quux2']], [("tup4_1", "tup_52"), ("t2up_1", "tup_32")], [{123:"one", 4432:"two"}, {144:"1one", 212:"1two"}]]


def to1DVector(threeDMatrix: list):
    
    oneDVector = list()

    for iterat in threeDMatrix:
        for y in list(itertools.chain(*iterat)):
            oneDVector.append(y)
        
    
    print("\n 1D Vector: ", oneDVector)
    return oneDVector
    


def convertIndex(i, j, k, m, p):
    
    index = i * m * p + j * p + k
    print("\n New Index is: ", index)
    return index
    
    

n = input("Enter size of the 3d matrix as 3 2 1: ")

length = n.split(" ")

n = int(length[0])
m = int(length[1])
p = int(length[2])

threeDMatrix = list()


for nn in range(n):
    for mm in range(m):
        mainList = list()
        for pp in range(p):
            mainList.append(input("Enter Element of [{}][{}][{}]: ".format(nn, mm, pp)))
        threeDMatrix.append(mainList)


print("Data Entered Successfully")


while(True):
        
    switchIndex = input('''
Choose function you need
1) Convert 3d Matrix to 1d Vector
2) Convert 3d Matrix index to 1d Vector index
''')
    
    if  switchIndex == '1' :
            to1DVector(threeDMatrix)
    elif switchIndex == '2':
            indciesString = input("Enter i j k indcies: ")
            indciesList = indciesString.split(" ")
            i = int(indciesList[0])
            j = int(indciesList[1])
            k = int(indciesList[2])
            convertIndex(i, j, k, m, p)
    
    print("\n***************************\n")
    
    
    