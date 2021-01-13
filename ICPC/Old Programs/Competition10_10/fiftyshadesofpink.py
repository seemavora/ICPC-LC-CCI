num = int(input())
colors = [str(input()) for i in range (num)]

def findColor(arr):
  counter = 0
  for x in range (num):
    place = arr[x].lower()
    if 'pink' in place or 'rose' in place:
      counter += 1
  if (counter>0):
    print(counter)
  else:
    print('I must watch Star Wars with my daughter')

findColor(colors)

 