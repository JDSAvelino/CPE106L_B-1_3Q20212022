import datetime


class CarRental:

    def __init__(self, availableCars=0):
        """
        Our constructor class that instantiates car rental shop.
        """

        self.availableCars = availableCars

    def displayavailableCars(self):
        """
        Displays the cars currently available for rent in the shop.
        """
        print("We have currently {} cars available to rent.".format(self.availableCars))
        return self.availableCars

    def rentCarOnHourlyBasis(self, n):
        """
        Rents a car on hourly basis to a customer.
        """
        if n <= 0:
            print("Number of cars should be positive!")
            return None

        elif n > self.availableCars:
            print("Sorry! We have currently {} cars available to rent.".format(self.availableCars))
            return None

        else:
            now = datetime.datetime.now()
            print("You have rented a {} car(s) on hourly basis today at {} hours.".format(n, now.hour))
            print("You will be charged $5 for each hour per car.")
            print("We hope that you enjoy our service.")

            self.availableCars -= n
            return now

    def rentCarOnDailyBasis(self, n):
        """
        Rents a car on daily basis to a customer.
        """
        if n <= 0:
            print("Number of cars should be positive!")
            return None

        elif n > self.availableCars:
            print("Sorry! We have currently {} cars available to rent.".format(self.availableCars))
            return None

        else:
            now = datetime.datetime.now()
            print("You have rented {} car(s) on daily basis today at {} hours.".format(n, now.hour))
            print("You will be charged $20 for each day per car.")
            print("We hope that you enjoy our service.")

            self.availableCars -= n
            return now

    def rentCarOnWeeklyBasis(self, n):
        """
        Rents a car on weekly basis to a customer.
        """
        if n <= 0:
            print("Number of cars should be positive!")
            return None

        elif n > self.availableCars:
            print("Sorry! We have currently {} cars available to rent.".format(self.availableCars))
            return None

        else:
            now = datetime.datetime.now()
            print("You have rented {} car(s) on weekly basis today at {} hours.".format(n, now.hour))
            print("You will be charged $60 for each week per car.")
            print("We hope that you enjoy our service.")
            self.availableCars -= n

            return now


class Customer:

    def __init__(self):
        """
        Our constructor method which instantiates various customer objects.
        """

        self.cars = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0

    def requestCar(self):
        """
        Takes a request from the customer for the number of cars.
        """

        cars = input("How many cars would you like to rent?")
        try:
            cars = int(cars)
        except ValueError:
            print("That's not a positive integer!")
            return -1

        if cars < 1:
            print("Invalid input. Number of cars should be greater than zero!")
            return -1
        else:
            self.cars = cars
        return self.cars

