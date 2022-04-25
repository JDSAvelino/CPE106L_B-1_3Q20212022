import unittest
from datetime import datetime, timedelta
from CarRental import CarRental, Customer


class CarRentalTest(unittest.TestCase):

    def test_Car_Rental_diplays_correct_availableCars(self):
        shop1 = CarRental()
        shop2 = CarRental(10)
        self.assertEqual(shop1.displayavailableCars(), 0)
        self.assertEqual(shop2.displayavailableCars(), 10)

    def test_rentCarOnHourlyBasis_for_negative_number_of_cars(self):
        shop = CarRental(10)
        self.assertEqual(shop.rentCarOnHourlyBasis(-1), None)

    def test_rentCarOnHourlyBasis_for_zero_number_of_cars(self):
        shop = CarRental(10)
        self.assertEqual(shop.rentCarOnHourlyBasis(0), None)

    def test_rentCarOnHourlyBasis_for_valid_positive_number_of_cars(self):
        shop = CarRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rentCarOnHourlyBasis(2).hour, hour)

    def test_rentCarOnHourlyBasis_for_invalid_positive_number_of_cars(self):
        shop = CarRental(10)
        self.assertEqual(shop.rentCarOnHourlyBasis(11), None)

    def test_rentCarOnDailyBasis_for_negative_number_of_cars(self):
        shop = CarRental(10)
        self.assertEqual(shop.rentCarOnDailyBasis(-1), None)

    def test_rentCarOnDailyBasis_for_zero_number_of_cars(self):
        shop = CarRental(10)
        self.assertEqual(shop.rentCarOnDailyBasis(0), None)

    def test_rentCarOnDailyBasis_for_valid_positive_number_of_cars(self):
        shop = CarRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rentCarOnDailyBasis(2).hour, hour)

    def test_rentCarOnDailyBasis_for_invalid_positive_number_of_cars(self):
        shop = CarRental(10)
        self.assertEqual(shop.rentCarOnDailyBasis(11), None)

    def test_rentCarOnWeeklyBasis_for_negative_number_of_cars(self):
        shop = CarRental(10)
        self.assertEqual(shop.rentCarOnWeeklyBasis(-1), None)

    def test_rentCarOnWeeklyBasis_for_zero_number_of_cars(self):
        shop = CarRental(10)
        self.assertEqual(shop.rentCarOnWeeklyBasis(0), None)

    def test_rentCarOnWeeklyBasis_for_valid_positive_number_of_cars(self):
        shop = CarRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rentCarOnWeeklyBasis(2).hour, hour)

    def test_rentCarOnWeeklyBasis_for_invalid_positive_number_of_cars(self):
        shop = CarRental(10)
        self.assertEqual(shop.rentCarOnWeeklyBasis(11), None)


if __name__ == '__main__':
    unittest.main()
