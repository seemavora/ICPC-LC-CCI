import numpy as np
inpt = str(input())
total = 0
value = {
  "IV":4,
  "IX":9,
  "XL":50,
  "XC":90,
  "CD":400,
  "CM":900,
  "I":1,
  "V":5,
  "X":10,
  "L":50,
  "C":100,
  "D":500,
  "M":1000
}
rom = list(value.keys())
for i in range(len(inpt)):
  print(total)
  inpt.count(str(rom[i]))
  total = total+ value.get(rom[i])
  inpt.replace(rom[i],'')
print(total)
