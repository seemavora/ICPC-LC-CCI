import sys
speciesArr = []
total = 0
for line in sys.stdin:
    speciesInput = line
    if '' == line.rstrip():
        break
    else:
        speciesArr.append(speciesInput)
        total += 1

species_dict= {i:('{:.6f}'.format(((speciesArr.count(i)/total))*100))for i in speciesArr}
# print(species_dict)
speciesDictItems = species_dict.items()
sortedSpecies = sorted(speciesDictItems)

for k, v in sortedSpecies:
  print(k.strip(), v)

# while True:
#     speciesInput = str(input())
#     if(speciesInput == ''):
#         break
#     else:
#         speciesArr.append(speciesInput)
# total = len(speciesArr)
# speciesArr.sort()
# species_dict= {i:('{:.6f}'.format(((speciesArr.count(i)/total))*100))for i in speciesArr}
# for k, v in species_dict.items():
#   print(k, v)
