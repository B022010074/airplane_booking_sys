from datetime import datetime
from os import system
import random
import sys

flightList = {"MH2580", "AK2341", "MH125", "AK236"}
fromList = {"Malaysia", "Japan", "Korea", "Italy", "Australia"}
toList = {"Indonesia", "Thailand", "UK", "America", "Brazil"}
gateList = {"A3", "A7", "B8", "C10"}
seatList = {
    "7K",
    "DO",
    "W5",
    "95",
    "Q8",
    "6R",
    "MH",
    "L0",
    "P4",
    "2N",
    "3D",
    "ED",
    "5U",
    "ZC",
    "Z7",
    "93",
    "8J",
    "55",
    "PH",
    "RN",
}


class Flight:
    flightNo = ""
    fromAirport = ""
    toAirport = ""
    date = datetime
    time = datetime
    gate = ""
    bookingId = 0

    def __init__(self, flightNo, fromAirport, toAirport, date, time, gate, id):
        self.flightNo = flightNo
        self.fromAirport = fromAirport
        self.toAirport = toAirport
        self.date = date
        self.time = time
        self.gate = gate
        self.bookingId = id


class Seat:
    seatNo = ""

    def __init__(self, seatNo):
        self.seatNo = seatNo


def avaiableSeats():
    global seatAvailable
    seatAvailable = 20


def passengers():
    global passengerNameList
    passengerNameList = []


def header(title):
    print(
        "Airline System (" + title + ")\n"
        "=======================\n"
    )


def _exit():
    header("Exit")
    print("Thank you for using our system!\n")
    #system("pause")
    sys.exit()
    #return


def booking():
    global seatAvailable
    global passengerNameList

    _nameList = []
    header("Booking")
    i = 0
    passengerNo = int(input("How many passenger(s): "))
    print("\n")

    if seatAvailable == 0:
        print("Sorry, the flight is fully booked\n")
        print("\n")
        #system("pause")
        #system("cls")
        #displayMenu()
        return

    if passengerNo > seatAvailable:
        print("Sorry, there are only " +
              str(seatAvailable) + " available seat(s)")
        print("\n")
        #system("pause")
        #system("cls")
        #displayMenu()
        return

    while i < passengerNo:
        name = input("Passenger " + str(i + 1) + " name: ")
        _nameList.append(name)
        passengerNameList.append(name)
        seatAvailable -= 1
        i += 1

    system("cls")
    header("Ticket")
    _ticketNo = 1

    for x in _nameList:
        print("\n")
        ticket(x, _ticketNo)
        _ticketNo += 1

    print("\n")
    #system("pause")
    #system("cls")
    #displayMenu()
    return

def ticket(passengerName, ticketNo):
    flight = Flight(
        random.choice(tuple(flightList)),
        random.choice(tuple(fromList)),
        random.choice(tuple(toList)),
        datetime.now().strftime("%d/%m/%y"),
        datetime.now().strftime("%H:%M:%S"),
        random.choice(tuple(gateList)),
        random.randint(10000, 99999),
    )
    seat = Seat(
        random.choice(tuple(seatList)),
    )
    print("Ticket " + str(ticketNo))
    print("======================================\n")
    print("\tBooking ID: " + str(flight.bookingId) + "\n")
    print("\tFlight No.: " + flight.flightNo + "\n")
    print("\tFrom: " + flight.fromAirport + "\n")
    print("\tTo: " + flight.toAirport + "\n")
    print("\tPassenger: " + passengerName + "\n")
    print("\tDate: " + str(flight.date) + "\n")
    print("\tTime: " + str(flight.time) + "\n")
    print("\tGate: " + flight.gate + "\n")
    print("\tSeat No.: " + seat.seatNo + "\n")
    print("======================================\n")
    return

def records():
    global passengerNameList
    header("Records")
    password = input("Please enter password: ")

    if password == "123":
        system("cls")
        header("Records")
        print("Seats Left: ", seatAvailable)
        print("\n")

        if len(passengerNameList) == 0:
            print("No records available")

        else:
            _ticketNo = 1
            for x in passengerNameList:
                ticket(x, _ticketNo)
                _ticketNo += 1

    else:
        print("\n")
        print("Invalid password!")

    print("\n")
    #system("pause")
    #system("cls")
    #displayMenu()
    return


def optionSelected(selection):
    if(selection==1):
        return booking()
    elif(selection==2):
        return records()
    elif(selection==3):
        return _exit()
    else:
        return print("Wrong number")

def displayMenu():
    selection=99
    while(selection!=3):
        header("Menu")
        print(
            "1.BOOKING\n"
            "2.RECORDS(Admin)\n"
            "3.EXIT\n\n"
        )

        selection = int(input("Enter your selection: "))
        optionSelected(selection)
        system("cls")
    return


def main():
    system("cls")
    avaiableSeats()
    passengers()
    displayMenu()

##    selection=99
##    while(selection!=3):
##        header("Menu")
##        print(
##            "1.BOOKING\n"
##            "2.RECORDS(Admin)\n"
##            "3.EXIT\n\n"
##        )
##
##        selection = int(input("Enter your selection: "))
##        optionSelected(selection)
##        #system("cls")
    return


main()
