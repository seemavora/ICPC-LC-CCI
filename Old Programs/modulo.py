nums = [int(input()) for i in range (10)]
modulo = []
for i in range (10):
  modulo.append(nums[i] % 42)

noDups = set(modulo)

print(len(noDups))