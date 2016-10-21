class trafficData:
	trafficList = []
	measurements = []
	#measurements = [oldMeasurement, newMeasurement]
	
	def __init__(self):
		self.trafficList = []
		self.measurements = []	

	def makeTrafficList(self,length,initMeasure):
	  #This function will initialize a the values for the list trafficList
	  #for len: see lenOfList (global)
	  #initMeasure = initial startup value for data on this agent
	  global lenOfList
	  #int len set to the number of entries you want to be able to add before it wraps around
	  #Ex: (8 hrs with a measurement every minute = 8*60*60 = 28800, so len == 28800
	  self.lenOfList = length
	  self.measurements.append(initMeasure)
	  #It is void

	def getSumOfTrafficList(self):
	  #This function will return the current sum of all entries in a given trafficList
	  sum = 0
	  for i in self.trafficList:
	    sum += i
	  #Returns the sum of the trafficList
	  return sum

	def getTrafficList(self):
	  #returns current trafficList
	  #WARNING: This could be a very large list!!!
	  return self.trafficList

	def updateTrafficList(self, newMeasurement):
	  #This function will get the difference between the measurement from
	  #the start of the period and the end of the period,
	  #and then append this to the list
	  if (len(self.measurements)<2): #First instance
	    self.updateMeasurements(newMeasurement)
	    tempDiff = self.measurements[1] - self.measurements[0]
	    return 0

	  self.updateMeasurements(newMeasurement)
	  tempDiff = self.measurements[1]- self.measurements[0]
	  if (len(self.trafficList)>self.lenOfList):
	    self.trafficList.pop(0)
	  self.trafficList.append(tempDiff)
	  #Returns the difference between measurement one and two
	  return (tempDiff)


	def updateMeasurements(self, newMeasurement):
	  #This function will update the measurements list
	  if len(self.measurements) >= 2:
	    self.measurements.pop(0)
	  self.measurements.append(newMeasurement)
	  #It is void



	
