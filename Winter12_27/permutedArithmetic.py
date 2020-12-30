numSeq = int(input())
sequence = []
numArr2 = []
def splitArr (arr):
  for i in range (len(arr)):
    tempStr = arr[i]
    arrList = (tempStr.split(' '))
    arrList.pop(0)
    # print(arrList)
    numArr = [int(i) for i in arrList]
    numArr.sort()
  numArr2.append(numArr)

  return numArr2
  # print(numArr2)
    

for i in range (numSeq):
  inputSeq = str(input())
  sequence.append(inputSeq)
  splitArr(sequence)
test = (splitArr(sequence))




