#https://open.kattis.com/problems/permutedarithmeticsequence
#solution uses numpy which is not accepted by kattis
import numpy as np
numSeq = int(input())
arr = []
for i in range (numSeq):
  inputSeq = str(input())
  arr.append(inputSeq)
# print(arr)

strArr = [] #initial array of values
resultArr = []
def sepArr(arr):
  for i in range (len(arr)):
    temp = arr[i] #input string
    newArr = temp.split(' ')
    x = np.array(newArr)
    y = x.astype(np.int)
    y = np.delete(y,0)
    # print(x)
    boolVal = (np.all((y[:-2] - y[1:-1]) == (y[1:-1] - y[2:])))
    if (boolVal == True):
      resultArr.append('arithmetic')
    else:
      y = np.sort(y)
      # print('new y: ')
      # print(y)
      boolVal = (np.all((y[:-2] - y[1:-1]) == (y[1:-1] - y[2:])))
      # print('new bool: '+ str(boolVal))
      if (boolVal == True):
        resultArr.append('permuted arithmetic')
      else:
        resultArr.append('non-arithmetic')
    # strArr.append(y)
  return(resultArr)

fin = (sepArr(arr))
for i in range (len(fin)):
  print(fin[i])