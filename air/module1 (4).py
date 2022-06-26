from datetime import datetime
from os import system
import random
import turtle

flightList = {"MH2580", "AK2341", "MH125", "AK236"}
fromList = {"Malaysia", "Japan", "Korea", "Italy", "Australia"}
toList = {"Indonesia", "Thailand", "UK", "America", "Brazil"}
gateList = {"A3", "A7", "B8", "C10"}
seatList = {"7K", "DO", "W5", "95", "Q8", "6R", "MH", "L0", "P4", "2N",
    "3D", "ED", "5U", "ZC", "Z7", "93", "8J", "55", "PH", "RN",
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
    file = open("NAME.txt","a")
    file.close()
    file = open("NAME.txt","r")
    count=0
    while True:
        line=file.readline()
        if len(line)==0:
            break
        count+=1
    seatAvailable = 20 - count
    file.close()

def passengers():
    global passengerNameList
    file = open("NAME.txt","a")
    file.close()
    file = open("NAME.txt","r")
    passengerNameList = file.readlines()
    file.close()

def header(title):
    print(
        "Airline System ( " + title + " )\n"
        "=======================\n"
    )


def _exit():
    header("Exit")
    print("Thank you for using our system!\n")
    return


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
        return

    if passengerNo > seatAvailable:
        print("Sorry, there are only " +
              str(seatAvailable) + " available seat(s)")
        print("\n")
        return

    while i < passengerNo:
        name = input("Passenger " + str(i + 1) + " name: ")

        print("\nLocation available:")
        print("\n" , fromList , "\n")
        fromwhere = input("Passenger " + str(i + 1) + " leaving from: ")

        print("\nLocation available:\n")
        print("\n" , toList , "\n")
        towhere = input("Passenger " + str(i + 1) + " going to: ")

        date = input("Passenger " + str(i + 1) + " date: ")

        print("\nSeat available:\n")
        print("\n" , seatList , "\n")
        seat = input("Passenger " + str(i + 1) + " seat: ")

        _nameList.append(name)
        passengerNameList.append(name)
        seatAvailable -= 1
        i += 1

    system("cls")
    header("Ticket")
    _ticketNo = 1

    for x in _nameList:
        print("\n")
        ticket(x, _ticketNo, fromwhere, towhere, date, seat)
        _ticketNo += 1

    print("\n")
    return

def ticket(passengerName, ticketNo, fromwhere, towhere, date, seat):
    flight = Flight(
        random.choice(tuple(flightList)),
        fromwhere,
        towhere,
        date,
        datetime.now().strftime("%H:%M:%S"),
        random.choice(tuple(gateList)),
        random.randint(10000, 99999),
    )
    seat = Seat(
        seat,
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

    f = open("RECORD.txt","a")
    g = open("NAME.txt","a")

    f.write(str(flight.bookingId) + "#" + flight.flightNo + "#" +
        flight.fromAirport + "#" + flight.toAirport + "#" + passengerName +
        "#" + flight.date + "#" + str(flight.time) + "#" + flight.gate + "#" +
        seat.seatNo + "#\n")

    g.write(passengerName+"\n")

    f.close()
    g.close()
    return

def records():
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
            readfile()

    else:
        print("\n")
        print("Invalid password!")

    return

def readfile():
    file=open("RECORD.txt","r")
    num=0
    while True:
        data=file.readline()
        x=data.split("#")
        if len(data)==0:
            break
        else:
            count=1
            print("Ticket " + str(num+1))
            print("======================================\n")
            for i in x:
                if count==1:
                    print("\tBooking ID: " + i + "\n")
                elif count==2:
                    print("\tFlight No.: " + i + "\n")
                elif count==3:
                    print("\tFrom: " + i + "\n")
                elif count==4:
                    print("\tTo: " + i + "\n")
                elif count==5:
                    print("\tPassenger: " + i + "\n")
                elif count==6:
                    print("\tDate: " + str(i) + "\n")
                elif count==7:
                    print("\tTime: " + str(i) + "\n")
                elif count==8:
                    print("\tGate: " + i + "\n")
                elif count==9:
                    print("\tSeat No.: " + i + "\n")
                    print("======================================\n")
                else:
                    pass
                count+=1
            num+=1
    file.close()

def optionSelected(selection):
    if(selection=="1"):
        return booking()
    elif(selection=="2"):
        return records()
    elif(selection=="3"):
        return _exit()
    else:
        return print("\nWrong number")

def displayMenu():
    selection=99
    while(selection!='3'):
        print("\n")
        header("Menu")
        print(
            "1.BOOKING\n"
            "2.RECORDS(Admin)\n"
            "3.EXIT\n\n"
        )

        selection = input("Enter your selection: ")
        optionSelected(selection)
    return


def main():
    avaiableSeats()
    passengers()
    displayMenu()

    return

def draw_circle(pen):
    # outer circle
    pen.setposition(0, -280)
    pen.pendown()
    pen.begin_fill()
    pen.color('red')
    pen.pencolor('white')
    pen.circle(300)
    pen.end_fill()
    pen.penup()

def draw_circle2(pen):
    # inner circle
    pen.pensize(2)
    pen.setposition(0, -230)
    pen.pendown()
    pen.begin_fill()
    pen.color('black')
    pen.circle(250)
    pen.end_fill()
    pen.penup()

def draw_body(pen):
    # drawing ‘A’
    pen.setposition(-70, -90)
    pen.pendown()
    pen.begin_fill()
    pen.color('red')
    pen.pensize(10)
    pen.pencolor('white')
    pen.left(30)
    pen.forward(370)
    pen.circle(20,140)
    pen.forward(70)
    pen.circle(110,45)
    pen.forward(265)
    pen.right(50)
    pen.forward(90)
    pen.left(55)
    pen.forward(50)
    pen.left(110)
    pen.forward(90)
    pen.circle(122,46)

    pen.end_fill()
    pen.penup()

def draw_wing1(pen):
    # Triangle shape in ‘A’ to make it look like 2d
    pen.pensize(10)
    pen.penup()
    pen.setposition(13, -30)

    pen.left(20)
    pen.forward(150)
    pen.right(125)

    pen.pendown()
    pen.begin_fill()
    pen.color('red')
    pen.pencolor('white')

    pen.forward(250)
    pen.right(50)
    pen.forward(60)
    pen.right(110)
    pen.forward(230)
    pen.end_fill()

def draw_wing2(pen):
    # arrow
    pen.pensize(10)
    pen.penup()
    pen.setposition(-33, 70)

    pen.pendown()
    pen.begin_fill()
    pen.color('red')
    pen.pencolor('white')

    pen.right(75)
    pen.forward(100)
    pen.left(125)
    pen.forward(120)
    pen.left(50)
    pen.forward(60)
    pen.left(110)
    pen.forward(105)
    pen.end_fill()

def drawairplane():
    win = turtle.Screen()
    win.bgcolor('black')

    pen = turtle.Turtle()
    pen.speed(10)
    pen.pensize(10)
    pen.penup()

    draw_circle(pen)
    draw_circle2(pen)
    draw_body(pen)
    draw_wing1(pen)
    draw_wing2(pen)
    pen.penup()

    #turtle.done()
    turtle.bye()

drawairplane()
main()
