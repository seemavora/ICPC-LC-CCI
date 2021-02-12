sampleArr = [1,2,3,4,5,6]
arrtotal = []
for i in range (len(sampleArr)):
  if i == 0:
    arrtotal.append(sampleArr[i])
  else:
    arrtotal.append(sampleArr[i] + arrtotal[i-1])
print(arrtotal)