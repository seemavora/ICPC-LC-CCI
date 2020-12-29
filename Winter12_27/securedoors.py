logLength = int(input())
logInput = []
logOutput =[]
inBuilding = set()

for x in range(logLength):
  initial = str(input())
  initialSplit = initial.split(" ")
  name = initialSplit[1]
  status = initialSplit[0]
  if name in inBuilding:
    if status == "exit":
      logOutput.append(name + " exited")
      inBuilding.remove(name)
    elif status == "entry":
      logOutput.append(name + " entered (ANOMALY)")
      inBuilding.add(name)
  elif name not in inBuilding:
    if status == "exit":
      logOutput.append(name + " exited (ANOMALY)")
    elif status == "entry":
      logOutput.append(name + " entered")
      inBuilding.add(name)
for i in range (len(logOutput)):
  print(logOutput[i])

# for x in range (logLength):
#   entExit = str(input())
#   logInput.append(entExit)
#   temp = entExit.split(" ")
#   name = temp[1]
#   status = temp[0]
#   if name in inBuilding and status == 'entry':
#     print("in")
#     logOutput.append(temp[1] +' entered (ANOMALY)')
#     inBuilding.add(str(temp[1]))
#   elif (name in inBuilding and status =='exit'):
#     print("in1")
#     logOutput.append(temp[1] +' exited')
#     inBuilding.remove(str(temp[1]))
#   elif (name not in inBuilding) and (status =='exit'):
#     print("in2")
#     logOutput.append(temp[1] +' exited (ANOMALY)')
#   elif (name in inBuilding and status =='entered'):
#     print("in3")
#     logOutput.append(temp[1] +' exited')
#     inBuilding.add(str(temp[1]))
# print(inBuilding)
# print(logOutput)