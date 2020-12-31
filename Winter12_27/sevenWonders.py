#https://open.kattis.com/contests/d2wwew/problems/sevenwonders
cards= str(input())
individualCard = list(cards)
tCount = 0
cCount = 0
gCount = 0
tcgCount = 0
for i in range (len(individualCard)):
  if individualCard[i]== 'T':
    tCount +=1
  elif individualCard[i] == 'C':
    cCount += 1
  elif individualCard[i] == 'G':
    gCount += 1
minCount = min(tCount, cCount, gCount)
if minCount ==0:
  extraPoint = 0
else: 
  extraPoint = minCount *7

finalSum = (tCount **2) + (cCount **2) + (gCount **2) + extraPoint
print(finalSum)