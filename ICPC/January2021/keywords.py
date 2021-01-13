# https://open.kattis.com/contests/jt9x2w/problems/keywords
numInputs = int(input())
keywords = []
for i in range (numInputs):
  keyInput = str(input())
  keyInput = keyInput.lower()
  keyInput = keyInput.replace('-', ' ')
  keywords.append(keyInput)
keywordsList = set(keywords)
uniqueItems = len(keywordsList)
print(uniqueItems)