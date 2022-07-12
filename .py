class Garage():
    def __init__(self, vacancy):
        values = list(range(1, vacancy + 1))
        self.parkingSpaces = values
        self.tickets = values[:]
        self.Ticket = dict()
        for spot in self.parkingSpaces:
            self.Ticket[spot] = ''
    def showSpaces(self):
        return "Current available spaces: " + str(len(self.parkingSpaces))
#Colt
    def takeTicket(self):
        if self.parkingSpaces and self.tickets:
            user_space = self.parkingSpaces.pop()
            self.Ticket[user_space] = False
            user_tickets = self.tickets.pop()
            print(f"Your parking space is {user_space}.\n"
                  + f"Your ticket number is {user_tickets}.")
        else:
            print("Parking lot has no vacancy.")
    def payForParking(self):
        ticket_number = int(input("Enter your ticket: "))
        paid = self.Ticket[ticket_number]
        if ticket_number in self.Ticket:
            if paid != '':
                print("Paid Ticket")
                if not paid:
                    input("Press 'Enter' to pay: ")
                    self.Ticket[ticket_number] = True
                    print("Your payment has been completed.")
                else:
                    print("Your ticket has been paid.")
                return ticket_number
            else:
                print("ERROR.")
                return -1
        else:
            print("Wrong Ticket.")
            return -1
#Dillon
    def leaveGarage(self):
        ticket_number = self.payForParking()
        if ticket_number == -1:
            print('Error wrong ticket.')
            return -1
        input("You have 15 minutes to leave. Press 'Enter' button to confirm: ")
        print("Thank you, have a nice day!")
        self.parkingSpaces.append(ticket_number)
        self.tickets.append(ticket_number)
    def run(self):
        while True:
            print("\n" + self.showSpaces())
            response = input("What do you want to do? You can: park, pay, leave, or quit. ")
            response = response.strip().lower()
            if response == 'park':
                self.takeTicket()
            elif response == 'pay':
                self.payForParking()
            elif response == 'leave':
                self.leaveGarage()
            elif response == 'quit':
                print("Thanks come again!")
                break
            else:
                print("Invalid command.")
garage = Garage(10)
print("Welcome to our garage")
garage.run()
#Dante