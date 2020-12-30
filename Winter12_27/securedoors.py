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

