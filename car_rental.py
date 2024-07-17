import datetime

class CarRental:
    def __init__(self, stock=0):
        self.stock = stock

    def display_cars(self):
        print(f"{self.stock} cars available to rent")

    def rent_car_hourly(self, n):
        if n <= 0:
            print("Number of cars should be positive")
            return None
        elif n > self.stock:
            print(f"Sorry, we have only {self.stock} cars available to rent")
            return None
        else:
            now = datetime.datetime.now()
            print(f"Rented {n} car(s) on hourly basis at {now.hour} hours")
            self.stock -= n
            return now

    def rent_car_daily(self, n):
        if n <= 0:
            print("Number of cars should be positive")
            return None
        elif n > self.stock:
            print(f"Sorry, we have only {self.stock} cars available to rent")
            return None
        else:
            now = datetime.datetime.now()
            print(f"Rented {n} car(s) on daily basis at {now.date()}")
            self.stock -= n
            return now

    def rent_car_weekly(self, n):
        if n <= 0:
            print("Number of cars should be positive")
            return None
        elif n > self.stock:
            print(f"Sorry, we have only {self.stock} cars available to rent")
            return None
        else:
            now = datetime.datetime.now()
            print(f"Rented {n} car(s) on weekly basis at {now.date()}")
            self.stock -= n
            return now

    def return_car(self, request):
        rentalTime, rentalBasis, numOfCars = request
        bill = 0

        if rentalTime and rentalBasis and numOfCars:
            self.stock += numOfCars
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime

            if rentalBasis == 1:  # hourly
                bill = round(rentalPeriod.seconds / 3600) * 5 * numOfCars
            elif rentalBasis == 2:  # daily
                bill = rentalPeriod.days * 20 * numOfCars
            elif rentalBasis == 3:  # weekly
                bill = (rentalPeriod.days // 7) * 60 * numOfCars

            if 3 <= numOfCars <= 5:
                print("You are eligible for a 30% discount")
                bill *= 0.7

            print(f"Thanks for returning your car(s). Your bill is ${bill}")
            return bill
        else:
            print("Are you sure you rented a car with us?")
            return None


class Customer:
    def __init__(self):
        self.cars = 0
        self.rentalBasis = 0
        self.rentalTime = 0

    def request_car(self):
        cars = input("How many cars would you like to rent? ")
        try:
            cars = int(cars)
        except ValueError:
            print("Number of cars should be a positive integer")
            return -1

        if cars < 1:
            print("Number of cars should be greater than zero")
            return -1
        else:
            self.cars = cars
        return self.cars

    def return_car(self):
        if self.rentalTime and self.rentalBasis and self.cars:
            return self.rentalTime, self.rentalBasis, self.cars
        else:
            return 0, 0, 0
