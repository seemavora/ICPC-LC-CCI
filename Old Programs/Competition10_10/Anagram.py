
numInputs = int(input())
anagram = [str(input()) for i in range (numInputs)]

def arrayPrint(arr):
  for x in arr:
    print(x)

def checkPanagram(arr):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  notIncluded = []
  for char in alphabet:
    if char not in (arr.lower()):
      if char not in notIncluded:
        notIncluded.append(char)
  if(len(notIncluded) > 0):
    print ('missing '+''.join(notIncluded))
  else:
    print('pangram')
    
for x in range (numInputs):
  place = anagram[x]
  checkPanagram(place)
  


  