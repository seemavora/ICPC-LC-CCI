x = int(input())
y = int(input())

posX = [1,4]
negX = [2,3]

if(x>0):
  quad = posX
else:
  quad = negX

if ((quad == posX) & (y > 0)):
  print(posX[0])
elif((quad == posX) & (y < 0)):
  print(posX[1])
elif ((quad == negX) & (y > 0)):
  print(negX[0])
else:
  print(negX[1])
