#https://open.kattis.com/problems/permutedarithmeticsequence
# testArr = ['2 3 4 5', '56 4 5 3 57 5', '588 7 4 5 321']
numSeq = int(input())
testarr = []
for i in range (numSeq):
  inputSeq = str(input())
  testarr.append(inputSeq)
def convertString(arr2):
  newArr = []
  for x in range (len(arr2)):
    temp= int(arr2[x])
    newArr.append(temp)
  return newArr

def splitArr(arr):
  finArr = []
  for i in range (len(arr)):
    temp = arr[i]
    strElem = temp.split(' ')
    finArr.append(convertString(strElem))
  return(finArr)

def checkSeq(arr):
  finalCheck = []
  for i in range (len(arr)):
    arr[i].pop(0)
    # print(arr[i])
    checkTF = all((i - j) == (j - k) for i, j, k in zip(arr[i][:-2], arr[i][1:-1], arr[i][2:]))
    if checkTF == True:
      finalCheck.append("arithmetic")
    else:
      arr[i].sort()
      checkTF = all((i - j) == (j - k) for i, j, k in zip(arr[i][:-2], arr[i][1:-1], arr[i][2:]))
      if checkTF == True:
        finalCheck.append("permuted arithmetic")
      else:
        finalCheck.append("non-arithmetic")
  return finalCheck

# print(splitArr(testArr))
resultArr = splitArr(testarr)
seqArrFin = (checkSeq(resultArr))
for i in range (len(seqArrFin)):
  print(seqArrFin[i])
