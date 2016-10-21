
trafficList = []
measurements = []
#measurements = [oldMeasurement, newMeasurement]


def makeTrafficList(length,initMeasure):
  #This function will initialize a the values for the list trafficList
  #for len: see lenOfList (global)
  #initMeasure = initial startup value for data on this agent
  global lenOfList
  #int len set to the number of entries you want to be able to add before it wraps around
  #Ex: (8 hrs with a measurement every minute = 8*60*60 = 28800, so len == 28800
  lenOfList = length
  measurements.append(initMeasure)
  #It is void

def getSumOfTrafficList():
  #This function will return the current sum of all entries in a given trafficList
  sum = 0
  for i in trafficList:
    sum += i
  #Returns the sum of the trafficList
  return sum

def getTrafficList():
  #returns current trafficList
  #WARNING: This could be a very large list!!!
  return trafficList

def updateTrafficList(newMeasurement):
  #This function will get the difference between the measurement from
  #the start of the period and the end of the period,
  #and then append this to the list
  if (len(measurements)<2): #First instance
    updateMeasurements(newMeasurement)
    tempDiff = measurements[1] - measurements[0]
    return 0

  updateMeasurements(newMeasurement)
  tempDiff = measurements[1]- measurements[0]
  if (len(trafficList)>lenOfList):
    trafficList.pop(0)
  trafficList.append(tempDiff)
  #Returns the difference between measurement one and two
  return (tempDiff)


def updateMeasurements(newMeasurement):
  #This function will update the measurements list
  if len(measurements) >= 2:
    measurements.pop(0)
  measurements.append(newMeasurement)
  #It is void

