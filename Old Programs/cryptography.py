ciphermessage = str(input())
cipher = str(input())
cipherMessNum = []
for letter in ciphermessage:
  number = ord(letter)-97
  cipherMessNum.append(number)
num = [] # the number for the final cipher
while len(num) <= len(ciphermessage):
  for letter in cipher:
    cipherNum = ord(letter)-97
    num.append(number)

