numInputs = int(input())
keywords = []
for i in range (numInputs):
  keyInput = str(input())
  keyInput = keyInput.lower()
  keyInput = keyInput.replace('-', ' ')
  # keyInput = keyInput.replace(' ','')
  keywords.append(keyInput)
keywordsList = set(keywords)
uniqueItems = len(keywordsList)
print(uniqueItems)