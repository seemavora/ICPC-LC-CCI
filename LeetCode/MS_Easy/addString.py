num1 = str(input())
num2 = str(input())
def strToInt(num):
  places = len(num)
  value = 0
  placeVal = places -1
  for i in range(places):
    digit = num[i]
    digit = int(digit)
    value = value+ digit * (10**placeVal)
    placeVal -= 1
  return value
num1Int = strToInt(num1)
num2Int = strToInt(num2)
total = num1Int + num2Int
print(total)