from collections import Counter
from collections import OrderedDict
# c = ['Seema', 'Shreya', 'Shruti', 'Seema']
# counter = Counter(c)
# print(dict(counter))

import sys
speciesArr = []

for line in sys.stdin:
    speciesInput = line
    if '' == line.rstrip():
        break
    else:
        speciesArr.append(speciesInput)
counter = Counter(speciesArr)
speciesDict = dict(counter)
speciesDictOrd = OrderedDict(sorted(speciesDict.items()))
print(speciesDictOrd)
total = sum(speciesDict.values())
keysList = list(speciesDictOrd.keys())
for i in range (len(keysList)):
  print(speciesDictOrd(i)
  # avg = '{:.6f}'.format((speciesDictOrd(keysList[i]) / total) *100)
  # speciesDictOrd[i] = avg
# print(species_dict)
for k, v in speciesDictOrd.items():
  print(k.strip(), v)

# from collections import OrderedDict 
  
# dict = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32'} 
# dict1 = OrderedDict(sorted(dict.items())) 
# print(dict1) 