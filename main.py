from getpass import getpass
www = getpass("Enter your password@mint : ")

securityCode = {}
matrixList = []
encodedMatrix = []
pattern = [
    [1,2,3],
    [1,1,2],
    [0,1,2]
]
pattern2 = [
    [0,1,-1],
    [2,-2,-1],
    [-1,1,1]
]
#This method with Initialize the securityCode like 'A':1, 'B':2... 'Z':26
def initializecode():
    code = 27
    for i in range(65,91):
        securityCode[chr(i)] = code
        code += 1
    node = 1
    for j in range(97,123):
        securityCode[chr(j)] = node
        node +=1
    kode=50
    for k in range(33,64):
        securityCode[chr(k)] = kode
        kode +=1
    securityCode[' '] = 200
#This method will find the character against a values
def findchar(value):
    for key in securityCode:
        if securityCode[key] is value:
            return key
#This method will find the value against a character
def findvalue(keyvalue):
    for key in securityCode:
        if key is keyvalue:
            return securityCode[key]
#Matrix Multiplication
def matrixmultiplication(mat1,mat2):
    mat = []
    for i in range(len(mat1)):
        total = 0
        for j in range(len(mat2)):
            total += mat1[i][j]*mat2[j]
        mat.append(total)
    return mat
#Encryption
def encryption(word):
    counter = 3
    start = 0
    end = 3
    matrix = []
    for c in word:
        matrix.append(findvalue(c))
    #print(matrix)
    while start < len(matrix):
        temp = matrix[start:end]
        if len(temp) is counter:
            matrixList.append(temp)
        else:
            for i in range(0,counter-len(temp)):
                temp.append(0)
            matrixList.append(temp)
        start += 3
        end += 3

    for mat in matrixList:
        encodedMatrix.append(matrixmultiplication(pattern,mat))

    matv=encodedMatrix
    print('Encrypted password:', encodedMatrix)
def decryption():

    for mat in matrixList:
        encodedMatrix.append(matrixmultiplication(pattern2,matv))

    print('Decrypted password', matrixList)

#MAIN FUNCTION
initializecode()
matv = {}
encryption(www)
decryption()
print(www)
