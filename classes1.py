class Flight:

    counter = 1

    def __init__(self, origin, destination, duration):
        
        #keep track of id number
        self.id = Flight.counter
        Flight.counter += 1

        #keep track of passengers
        self.passengers = []
        
        self.origin = origin
        self.destination = destination
        self.duration = duration
    
    def print_info(self):
        print(f"Flight id: {self.id}")
        print(f"Flight origin: {self.origin}")
        print(f"FLight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")

        print()
        print("Passengers:")
        for passenger in self.passengers:
            print(f"Passenger: {passenger.name} in flight with id {passenger.flight_id}")

    def delay(self, amount):
        self.duration += amount

    def add_passenger(self,p):
        self.passengers.append(p)
        p.flight_id = self.id

class Passenger:

    def __init__(self, name):
        self.name = name

def main():

    # create flight
    f = Flight(origin="New York", destination="Paris", duration=540)

    # change the value of a duration
    f.duration += 30

    # print details of a flight
    print(f.origin)
    print(f.destination)
    print(f.duration)

    f1 = Flight(origin="New York", destination="India", duration=1240)
    p1 = Passenger("Alice")
    p2 = Passenger("Brian")
    f1.add_passenger(p1)
    f1.add_passenger(p2)

    f1.print_info()

    f1.delay(100)
    print()

    f1.print_info()

if __name__ == "__main__":
    main()
