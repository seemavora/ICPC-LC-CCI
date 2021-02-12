vowelString = str(input())
vowels = ['a','e','i','o','u']
for i in range (len(vowels)):
  vowelString = vowelString.replace(vowels[i],'')
print(vowelString)

