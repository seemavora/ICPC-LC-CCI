speciesArr = []

while True:
    speciesInput = str(input())
    if(speciesInput == ''):
        break
    else:
        speciesArr.append(speciesInput)
total = len(speciesArr)
speciesArr.sort()
species_dict= {i:('{:.6f}'.format(((speciesArr.count(i)/total))*100))for i in speciesArr}
for k, v in species_dict.items():
  print(k, v)
