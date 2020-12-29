givenSent = str(input())
sentArr = givenSent.split(' ')
sentSet = set(sentArr)
if len(sentArr) == len(sentSet):
  print("yes")
else:
  print("no")
