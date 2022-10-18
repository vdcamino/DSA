class Passenger:
    def __init__(self):
        self.lastCheckInStation = ""
        self.lastCheckInTime = 0
        self.lastCheckOutStation = ""
        self.lastCheckOutTime = 0

    def checkIn(self, startTime, startStation):
        self.lastCheckInTime = startTime
        self.lastCheckInStation = startStation

    def checkOut(self, endTime, endStation):
        self.lastCheckOutTime = endTime
        self.lastCheckOutStation = endStation

    def getTravelDuration(self):
        return self.lastCheckOutTime - self.lastCheckInTime

    def getTravelRoute(self):
        return self.lastCheckInStation + "#" + self.lastCheckOutStation


class Route:
    def __init__(self, startStation, endStation):
        self.tripsCount = 0
        self.averageDuration = 0

    def addTrip(self, tripDuration):
        # work with percentages to avoid overflow
        newContribution = 1 / (1 + self.tripsCount)
        oldContribution = 1 - newContribution

        self.averageDuration = (
            oldContribution * self.averageDuration + newContribution * tripDuration
        )
        self.tripsCount += 1

    def getAverage(self):
        return self.averageDuration


class UndergroundSystem:
    def __init__(self):
        self.routes = {}  # key = startStation + "#" + endStation, val = Route
        self.passengers = {}  # key = userId, val = Passenger

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.passengers:
            newPassenger = Passenger()
            self.passengers[id] = newPassenger
        self.passengers[id].checkIn(t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.passengers[id].checkOut(t, stationName)
        travelDuration = self.passengers[id].getTravelDuration()
        travelRoute = self.passengers[id].getTravelRoute()

        if travelRoute not in self.routes:
            startStation, endStation = travelRoute.split("#")
            newRoute = Route(startStation, endStation)
            self.routes[travelRoute] = newRoute

        self.routes[travelRoute].addTrip(travelDuration)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        routeKey = startStation + "#" + endStation
        return self.routes[routeKey].getAverage()


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
