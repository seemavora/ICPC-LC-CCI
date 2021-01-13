tile = int(input())
rows, cols = (tile, tile) 
arr=[] 
for i in range(cols): 
    col = [] 
    for j in range(rows): 
        col.append(str(input())) 
    arr.append(col) 

countRow = 0
countCol = 0
for i in range(cols):
  if (arr[i]=='W' or arr[i]=='B'):
      countCol+= 1
      checkVal(countCol)
  else:
      countCol= 0
  for j in range(rows):
    if (arr[j]=='W' or arr[j]=='B'):
      countRow += 1
      checkVal(countCol)
    else:
      countRow = 0
    
def checkVal(x):
  if x >3:
    breakOut = True
  else:
    breakOut = False
  return breakOut

if breakOut == True:
  print(0)
  

