from enum import Enum
import time


class ParkingTicketStatus(Enum):
    PAID = 1
    UNPAID = 2


class ParkingSpaceStatus(Enum):
    FREE = 1
    TAKEN = 2


class VehicleSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class PaymentType(Enum):
    CARD = 1
    CASH = 2


class ParkingSpaceType(Enum):
    BIKE_PARKING = 1
    CAR_PARKING = 2
    TRUCK_PARKING = 3


class PaymentStatus(Enum):
    PENDING = 1
    SUCCESS = 2
    CANCELLED = 3
    REFUNDED = 4
    UNPAID = 5


class Vehicle:
    def __init__(self):
        self.type = None
        self.plate = None
        self.parkingTicket = None
        self.payments = []


class ParkingLot:
    def __init__(self, address, name):
        self.parkingFloors = []
        self.entrances = []
        self.exits = []
        self.address = address
        self.name = name

        def isParkingSporAvailableForVehicle(self, vehicle: Vehicle):
            return None

        def updateParkingAttendant(
            self, parkingAttendant: ParkingAttendant, gateId: int
        ):
            return None


class ParkingFloor:
    def __init__(self):
        self.levelId = None
        self.isFull = False
        self.parkingSpaces = []
        self.parkingDisplayBoard = None


class ParkingTicket:
    def __init__(self):
        self.entryTime = time.time()
        self.exitTime = None
        self.levelId = None
        self.spotId = None
        self.parkingSpaceType = None
        self.totalCost = 0
        self.parkingTicketStatus = None

        def updateTotalCost(self):
            return None

        def updateVehicleExitTime(self, vehicleExitDateTime):
            return None


class Gate:
    def __init__(self):
        self.gateId = None
        self.parkingAttendant = None


class Entrance(Gate):
    def __init__(self):
        super().__init__()

    def getParkingTicket(self, vehicle: Vehicle):
        # return ParkingTicket object based on vehicle type
        return None


class Exit(Gate):
    def __init__(self):
        super().__init__()

    def payForParking(self, parkingTicket: ParkingTicket):
        # return ParkingTicket object updated (all necessary information is contained in the parkingTicket object)
        return None


class Address:
    def __init__(self):
        self.country = None
        self.state = None
        self.street = None
        self.zipCode = None


class ParkingSpace(Enum):
    def __init__(self):
        self.id = None
        self.isFree = True
        self.type = None


class ParkingDisplayBoard:
    def __init__(self):
        self.spotsAvailablePerFloor = {}

    def updateFreeSpotsAvailable(self, parkingSpace: ParkingSpace):
        return None


class Account:
    def __init__(self):
        self.name = None
        self.email = None
        self.password = None
        self.phone = None
        self.address = None


class Admin(Account):
    def __init__(self):
        super().__init__()

    def addParkingFloor(self, parkingLot: ParkingLot, parkingFloor: ParkingFloor):
        return None

    def addParkingSpace(self, parkingFloor: ParkingFloor, parlingSpace: ParkingSpace):
        return None

    def addParkingDisplayBoard(
        self, parkingFloor: ParkingFloor, parkingDisplayBoard: ParkingDisplayBoard
    ):
        return None


class ParkingAttendant(Account):
    def __init__(self):
        super().__init__()
        self.gateId = None

    def processVehicleEntry(self, vehicle: Vehicle, entry: Entrance):
        return None

    def processPayment(self, parkingTicket: ParkingTicket, exit: Exit):
        return None


class Payment:
    def __init__(self):
        self.amount = None
        self.type = None
        self.date = None
        self.parkingTicket = None
        self.status = None

    def makePayment(self, ticket: ParkingTicket, paymentType: PaymentType):
        return None
