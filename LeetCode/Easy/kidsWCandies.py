currentCandies = [12,1,12]
extraCandies = 10
boolArr = []
maxCand = max(currentCandies)
for i in range (len(currentCandies)):
  if currentCandies[i] + extraCandies >= maxCand:
    boolArr.append(True)
  else:
    boolArr.append(False)
print(boolArr)