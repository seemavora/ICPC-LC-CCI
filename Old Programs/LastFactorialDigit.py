import math

testcases = int(input())
factorial = [int(input()) for i in range (testcases)]
# for j in range (testcases):
#   value = factorial[j-1]
for k in range(testcases):
  valInArray = factorial[k]
  fact = (math.factorial(valInArray))
  print(fact %10)


 
  



