# Object-Oriented Program that simulates a parking garage with the following Methods:
# Ticket and parking space counter with 20 available spots
# Payment kiosk that allows for payment at entrance or exit of garage

class ParkingGarage():

    def __init__(self):
        self.tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                         11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.parkingSpaces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                         11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.currentTicket = {"paid": True}

    # Method to takeTicket, and pop() tickets and parkingSpaces.
    def takeTicket(self):
        self.tickets.pop()
        self.parkingSpaces.pop()
        print("Take your ticket, and enjoy your parking.\n")
    
    # Method to pay for parking.
    # If payment is $3, then a ticket is issued so users do not pay twice upon leaving.
    # If user would rather pay upon leaving, they have the option to do that.
    def payForParking(self):
        print("Welcome to the Brown Trout Parking Garage! We have issued you your ticket for parking. The fee is $3.\n")
        while True:
            payment = input("You may pay now if you wish. Enter 3 to pay $3 for your ticket, or you can pay upon leaving by entering 'defer': ")
            if payment == '3':
                print("Thank you for your payment, you have 15min to leave.\n")
                self.currentTicket["paid"] = True
                break
            elif payment == "defer":
                print("Thank you, please proceed forward.\n")
                self.currentTicket["paid"] = False
                break
            else:
                print("Please enter the correct amount, or 'defer' to pay upon leaving.\n")
    
    # method for leaving the garage
    # Makes sure ticket is paid for, and appends spaces back into parkingSpaces() and currentTicket()
    def leaveGarage(self):
        if self.currentTicket["paid"] == True:
            print("Thank You, have a nice day!\n")
            self.parkingSpaces.append(1)
            self.tickets.append(1)
        elif self.currentTicket["paid"] == False:
            while True:
                print("It looks like you are ready to leave.")
                payment = input("Please enter 3 to pay $3 before leaving: $")
                if payment == '3':
                    print("Thank you for your payment, have a nice day!\n")
                    self.parkingSpaces.append(1)
                    self.tickets.append(1)
                    break
                else:
                    print("Please enter the correct amount")
            
garage = ParkingGarage()
garage.takeTicket()
# print("Number of available tickets: ",garage.tickets)
# print("Number of available parking spaces: ",garage.parkingSpaces)
garage.payForParking()
garage.leaveGarage()