testCases = int(input())
numPlaces = []
for i in range (testCases):
  worktrips = int(input())
  placesArr = []
  for j in range (worktrips):
    places = str(input())
    placesArr.append(places)
  setPlacesArr = set(placesArr)
  numPlaces.append(len(setPlacesArr))
for i in range (testCases):
  print(numPlaces[i])
